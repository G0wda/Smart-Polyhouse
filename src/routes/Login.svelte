<script>
  import { navigate } from "svelte-routing";
  import { Link } from "svelte-routing";
  
  let username = "";
  let password = "";
  
  const handleSubmit = (e) => {
    e.preventDefault();
    // TODO: Add actual authentication logic
    navigate("/dashboard");
  };

  const handleRegister = (e) => {
    e.preventDefault();
    // TODO: Add actual authentication logic
    navigate("/register");
  };
</script>

<div class="min-h-screen flex items-center justify-center bg-gray-100">
  <div class="bg-white p-8 rounded-lg shadow-md w-96">
    <h2 class="text-2xl font-bold mb-6 text-center">Login</h2>
    
    <form on:submit={handleSubmit}>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
          Username
        </label>
        <input
          bind:value={username}
          type="text"
          id="username"
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
          required
        />
      </div>
      
      <div class="mb-6">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
          Password
        </label>
        <input
          bind:value={password}
          type="password"
          id="password"
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
          required
        />
      </div>
      
      <button
        type="submit"
        class="w-full bg-green-500 text-white py-2 rounded-lg hover:bg-green-600 transition-colors"
      >
        Login
      </button>
    </form>

    <p class="text-center text-sm text-gray-600 mt-4">
      Don't have an account? 
      <button on:click={handleRegister}>Register</button>
    </p>
  </div>
</div>
