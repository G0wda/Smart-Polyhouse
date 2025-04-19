<script>
  import { navigate } from "svelte-routing";

  let username = "";
  let email = "";
  let password = "";
  let confirmPassword = "";

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      alert("Passwords do not match!");
      return;
    }

    try {
      const res = await fetch("http://localhost:3000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, email, password }),
      });

      const data = await res.json();

      if (res.ok) {
        alert("Registration successful!");
        navigate("/login");
      } else {
        alert(data.message || "Registration failed.");
      }
    } catch (err) {
      alert("An error occurred.");
    }
  };
</script>

<div class="min-h-screen flex items-center justify-center bg-gray-100">
  <div class="bg-white p-8 rounded-lg shadow-md w-96">
    <h2 class="text-2xl font-bold mb-6 text-center">Register</h2>

    <form on:submit={handleSubmit}>
      <div class="mb-4">
        <!-- svelte-ignore a11y-label-has-associated-control -->
        <label class="block text-gray-700 text-sm font-bold mb-2">Username</label>
        <input bind:value={username} type="text" required class="w-full px-3 py-2 border rounded-lg" />
      </div>

      <div class="mb-4">
        <!-- svelte-ignore a11y-label-has-associated-control -->
        <label class="block text-gray-700 text-sm font-bold mb-2">Email</label>
        <input bind:value={email} type="email" required class="w-full px-3 py-2 border rounded-lg" />
      </div>

      <div class="mb-4">
        <!-- svelte-ignore a11y-label-has-associated-control -->
        <label class="block text-gray-700 text-sm font-bold mb-2">Password</label>
        <input bind:value={password} type="password" required class="w-full px-3 py-2 border rounded-lg" />
      </div>

      <div class="mb-6">
        <!-- svelte-ignore a11y-label-has-associated-control -->
        <label class="block text-gray-700 text-sm font-bold mb-2">Confirm Password</label>
        <input bind:value={confirmPassword} type="password" required class="w-full px-3 py-2 border rounded-lg" />
      </div>

      <button type="submit" class="w-full bg-green-500 text-white py-2 rounded-lg hover:bg-green-600">
        Register
      </button>
    </form>
  </div>
</div>
