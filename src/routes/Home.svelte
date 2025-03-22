<script>
  import { navigate } from "svelte-routing";
  
  const handleLogin = () => {
    navigate("/login");
  };
</script>

<div class="min-h-screen flex flex-col items-center justify-center bg-cover bg-center bg-no-repeat" style="background-image: url('https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?q=80&w=2000&auto=format&fit=crop');">
  <div class="bg-black bg-opacity-50 w-full h-full absolute top-0 left-0"></div>
  <div class="text-center relative z-10">
    <h1 class="text-5xl font-bold text-white mb-8">Smart Polyhouse</h1>
    <p class="text-xl text-white mb-8">Intelligent Irrigation Management System</p>
    <button
      on:click={handleLogin}
      class="bg-white text-green-500 px-8 py-3 rounded-full font-semibold hover:bg-green-50 transition-colors transform hover:scale-105"
    >
      Login
    </button>
  </div>
  
  <div class="absolute bottom-0 w-full flex justify-center z-10">
    <div class="plant-animation">
      🌱
    </div>
  </div>
</div>

<style>
  .plant-animation {
    font-size: 4rem;
    animation: grow 3s infinite;
  }
  
  @keyframes grow {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
  }
</style>