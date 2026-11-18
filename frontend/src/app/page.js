
"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [tasks, setTasks] = useState([]);
  const [selectedTask, setSelectedTask] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/tasks/")
      .then((response) => {
        if (!response.ok) throw new Error("Failed to load tasks");
        return response.json();
      })
      .then((data) => setTasks(data))
      .catch(() => setError("Unable to connect to the backend."))
      .finally(() => setLoading(false));
  }, []);

  return (
    <main className="container">
      <header>
        <h1>Adzzat Labs</h1>
        <p>Full-Stack Engineering Task Platform</p>
      </header>

      <section className="hero">
        <h2>Explore Engineering Tasks</h2>
        <p>Practice solving real-world software engineering problems.</p>
      </section>

      <h2>Available Tasks</h2>

      {loading && <p>Loading tasks...</p>}
      {error && <p>{error}</p>}

      <div className="task-grid">
        {tasks.map((task) => (
          <article className="task-card" key={task.id}>
            <span>{task.type}</span>
            <h3>{task.title}</h3>
            <p>{task.description}</p>
            <p>Difficulty: {task.difficulty}</p>
            <button onClick={() => setSelectedTask(task)}>
              View Details
            </button>
          </article>
        ))}
      </div>

      {selectedTask && (
        <div className="modal">
          <div className="modal-content">
            <button
              className="close"
              onClick={() => setSelectedTask(null)}
            >
              Close
            </button>

            <h2>{selectedTask.title}</h2>
            <p>{selectedTask.statement}</p>

            <h3>Environment</h3>
            <ul>
              {selectedTask.environment?.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>

            <p>Difficulty: {selectedTask.difficulty}</p>
          </div>
        </div>
      )}
    </main>
  );
}
