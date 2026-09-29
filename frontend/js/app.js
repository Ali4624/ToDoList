const API = "/api";
let currentUser = null;

const authPage = document.getElementById("auth-page");
const dashboardPage = document.getElementById("dashboard-page");
const loginForm = document.getElementById("login-form");
const registerForm = document.getElementById("register-form");
const authError = document.getElementById("auth-error");
const tabBtns = document.querySelectorAll(".tab-btn");
const welcomeUser = document.getElementById("welcome-user");
const createForm = document.getElementById("create-form");
const createError = document.getElementById("create-error");
const todosList = document.getElementById("todos-list");
const taskStats = document.getElementById("task-stats");
const charCounter = document.getElementById("char-counter");
const profileModal = document.getElementById("profile-modal");
const profileForm = document.getElementById("profile-form");
const profileError = document.getElementById("profile-error");

function showError(el, msg) {
    el.textContent = msg;
    el.classList.remove("hidden");
}

function hideError(el) {
    el.classList.add("hidden");
}

async function api(path, options = {}) {
    const res = await fetch(API + path, {
        headers: { "Content-Type": "application/json" },
        ...options,
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Request failed");
    return data;
}

function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
}

// ── Auth tabs with Water Drop Switch Animation ──

const authTabs = document.querySelector(".auth-tabs");
const tabDroplet = document.getElementById("tab-droplet");

tabBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
        if (btn.classList.contains("active")) return;
        const currentActive = document.querySelector(".tab-btn.active");
        const currentTab = currentActive ? currentActive.dataset.tab : "login";
        const targetTab = btn.dataset.tab;

        // Animate fluid water droplet stretch in direction of motion
        if (tabDroplet) {
            tabDroplet.classList.remove("sliding-right", "sliding-left");
            void tabDroplet.offsetWidth; // Force reflow to cleanly trigger animation
            if (targetTab === "register" && currentTab === "login") {
                tabDroplet.classList.add("sliding-right");
            } else if (targetTab === "login" && currentTab === "register") {
                tabDroplet.classList.add("sliding-left");
            }
        }

        if (authTabs) {
            authTabs.dataset.active = targetTab;
        }

        // Spawn liquid water ripple at click spot
        const rect = btn.getBoundingClientRect();
        const ripple = document.createElement("span");
        ripple.className = "water-ripple";
        const size = Math.max(rect.width, rect.height);
        ripple.style.width = ripple.style.height = `${size}px`;
        ripple.style.left = `${(e.clientX - rect.left) - size / 2}px`;
        ripple.style.top = `${(e.clientY - rect.top) - size / 2}px`;
        btn.appendChild(ripple);
        setTimeout(() => ripple.remove(), 600);

        tabBtns.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        loginForm.classList.toggle("hidden", targetTab !== "login");
        registerForm.classList.toggle("hidden", targetTab !== "register");
        hideError(authError);
    });
});

// ── Login ──

loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    hideError(authError);
    try {
        const data = await api("/auth/login", {
            method: "POST",
            body: JSON.stringify({
                username: document.getElementById("login-username").value.trim(),
                password: document.getElementById("login-password").value,
            }),
        });
        enterDashboard(data.username);
    } catch (err) {
        showError(authError, err.message);
    }
});

// ── Register ──

registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    hideError(authError);
    const username = document.getElementById("reg-username").value.trim();
    const password = document.getElementById("reg-password").value;

    if (username.length < 8 || !/\d/.test(username)) {
        showError(authError, "Username must be at least 8 characters and contain a digit.");
        return;
    }
    if (password.length < 8 || !/\d/.test(password)) {
        showError(authError, "Password must be at least 8 characters and contain a digit.");
        return;
    }

    try {
        const data = await api("/auth/register", {
            method: "POST",
            body: JSON.stringify({ username, password }),
        });
        enterDashboard(data.username);
    } catch (err) {
        showError(authError, err.message);
    }
});

// ── Character counter ──

document.getElementById("task-input").addEventListener("input", (e) => {
    const len = e.target.value.length;
    charCounter.textContent = `${len} / 50`;
    charCounter.className = "char-counter" + (len >= 50 ? " limit" : len >= 40 ? " warn" : "");
});

// ── Dashboard ──

function enterDashboard(username) {
    currentUser = username;
    authPage.classList.add("hidden");
    dashboardPage.classList.remove("hidden");
    welcomeUser.textContent = `Hello, ${username}`;
    loadTodos();
}

document.getElementById("logout-btn").addEventListener("click", () => {
    currentUser = null;
    dashboardPage.classList.add("hidden");
    authPage.classList.remove("hidden");
    loginForm.reset();
    registerForm.reset();
    hideError(authError);
    if (authTabs) authTabs.dataset.active = "login";
    if (tabDroplet) tabDroplet.classList.remove("sliding-right", "sliding-left");
    tabBtns.forEach((b) => b.classList.toggle("active", b.dataset.tab === "login"));
    loginForm.classList.remove("hidden");
    registerForm.classList.add("hidden");
});

// ── Todos ──

async function loadTodos() {
    todosList.innerHTML = '<div class="loading"><div class="spinner"></div></div>';
    try {
        const todos = await api(`/todos/${currentUser}`);
        renderTodos(todos);
    } catch (err) {
        todosList.innerHTML = `<div class="empty-msg"><p>${escapeHtml(err.message)}</p></div>`;
        taskStats.classList.add("hidden");
    }
}

function renderTodos(todos) {
    if (!todos.length) {
        todosList.innerHTML = `
            <div class="empty-msg">
                <div class="empty-icon-wrap">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="12" y1="8" x2="12" y2="12"></line>
                        <line x1="12" y1="16" x2="12.01" y2="16"></line>
                    </svg>
                </div>
                <p class="empty-title">No tasks yet</p>
                <p class="empty-subtitle">Create one above to start planning your day!</p>
            </div>`;
        taskStats.classList.add("hidden");
        return;
    }

    const counts = { PENDING: 0, COMPLETED: 0, CANCELLED: 0 };
    todos.forEach((t) => { counts[t.status] = (counts[t.status] || 0) + 1; });

    taskStats.classList.remove("hidden");
    taskStats.innerHTML = `
        <div class="stat"><span class="stat-num">${todos.length}</span><span class="stat-label">Total</span></div>
        <div class="stat"><span class="stat-num pending">${counts.PENDING}</span><span class="stat-label">Pending</span></div>
        <div class="stat"><span class="stat-num completed">${counts.COMPLETED}</span><span class="stat-label">Done</span></div>
        <div class="stat"><span class="stat-num cancelled">${counts.CANCELLED}</span><span class="stat-label">Cancelled</span></div>
    `;

    todosList.innerHTML = todos
        .map((t) => {
            const status = t.status || "PENDING";
            const statusClass = status === "COMPLETED" ? "completed" : status === "CANCELLED" ? "cancelled" : "pending";
            const badgeClass = "status-" + statusClass;

            const actions = status === "PENDING"
                ? `<button class="btn btn-sm btn-success" onclick="setStatus(${t.taskId}, 'COMPLETED')">
                     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                     <span>Complete</span>
                   </button>
                   <button class="btn btn-sm btn-warning" onclick="setStatus(${t.taskId}, 'CANCELLED')">
                     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                     <span>Cancel</span>
                   </button>`
                : status === "CANCELLED"
                    ? `<button class="btn btn-sm btn-glass" onclick="setStatus(${t.taskId}, 'PENDING')">
                         <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="1 4 1 10 7 10"></polyline><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"></path></svg>
                         <span>Reopen</span>
                       </button>`
                    : "";

            return `
            <div class="todo-card ${statusClass}">
                <div class="todo-top">
                    <span class="todo-task">${escapeHtml(t.task)}</span>
                    <span class="todo-id">#${t.taskId}</span>
                </div>
                <div class="todo-meta">
                    <span>
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                        ${escapeHtml(t.creationTime)}
                    </span>
                    <span>
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                        Due: ${escapeHtml(t.expectedCompletion)}
                    </span>
                    <span class="status-badge ${badgeClass}">${status}</span>
                </div>
                <div class="todo-actions">
                    ${actions}
                    <button class="btn btn-sm btn-danger" onclick="deleteTodo(${t.taskId})">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                        <span>Delete</span>
                    </button>
                </div>
            </div>`;
        })
        .join("");
}

// ── Create todo ──

createForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    hideError(createError);
    const task = document.getElementById("task-input").value.trim();
    const dueDate = document.getElementById("due-date-input").value;

    if (task.length > 50) {
        showError(createError, "Task description cannot exceed 50 characters.");
        return;
    }

    try {
        await api(`/todos/${currentUser}`, {
            method: "POST",
            body: JSON.stringify({ task, due_date: dueDate }),
        });
        createForm.reset();
        charCounter.textContent = "0 / 50";
        charCounter.className = "char-counter";
        loadTodos();
    } catch (err) {
        showError(createError, err.message);
    }
});

// ── Status & delete ──

async function setStatus(todoId, status) {
    try {
        await api(`/todos/${todoId}/status`, {
            method: "PATCH",
            body: JSON.stringify({ status }),
        });
        loadTodos();
    } catch (err) {
        alert(err.message);
    }
}

async function deleteTodo(todoId) {
    if (!confirm("Delete this task?")) return;
    try {
        await api(`/todos/${todoId}`, { method: "DELETE" });
        loadTodos();
    } catch (err) {
        alert(err.message);
    }
}

document.getElementById("refresh-btn").addEventListener("click", loadTodos);

// ── Profile modal ──

document.getElementById("profile-btn").addEventListener("click", async () => {
    profileModal.classList.remove("hidden");
    hideError(profileError);
    try {
        const p = await api(`/auth/profile/${currentUser}`);
        document.getElementById("profile-name").value = p.name || "";
        document.getElementById("profile-gender").value = p.gender || "";
        document.getElementById("profile-bday").value = p.birthday || "";
    } catch {
        // profile not set yet
    }
});

document.getElementById("close-modal").addEventListener("click", () => {
    profileModal.classList.add("hidden");
});

profileModal.addEventListener("click", (e) => {
    if (e.target === profileModal) profileModal.classList.add("hidden");
});

profileForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    hideError(profileError);
    const name = document.getElementById("profile-name").value.trim();
    const gender = parseInt(document.getElementById("profile-gender").value) || 0;
    const birthday = document.getElementById("profile-bday").value;

    try {
        await api(`/auth/profile/${currentUser}`, {
            method: "PUT",
            body: JSON.stringify({ name, gender, birthday }),
        });
        profileModal.classList.add("hidden");
    } catch (err) {
        showError(profileError, err.message);
    }
});
