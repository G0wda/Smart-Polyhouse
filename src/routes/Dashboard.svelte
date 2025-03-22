<script>
  import { navigate } from "svelte-routing";
  import { Leaf } from 'lucide-svelte';


  let searchQuery = "";
  let plants = [];

  const mockPlants = [
    { id: 1, name: "Tomato", temp: 25, moisture: 60, npk: "21-20-20" },
    { id: 2, name: "Cucumber", temp: 23, moisture: 65, npk: "25-15-15" },
    { id: 3, name: "Lettuce", temp: 20, moisture: 70, npk: "10-10-10" }
  ];

  // Show all plants initially
  plants = mockPlants;

  // Update displayed plants when searchQuery changes
  $: plants = searchQuery
    ? mockPlants.filter(plant =>
        plant.name.toLowerCase().includes(searchQuery.toLowerCase())
      )
    : mockPlants;

  const handlePlantClick = (id) => {
    navigate(`/plant/${id}`);
  };
</script>

<div class="min-h-screen p-8 bg-cover bg-center bg-no-repeat" 
     style="background-image: url('https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?q=80&w=2000&auto=format&fit=crop');">
  <div class="bg-white bg-opacity-90 min-h-screen p-8 rounded-lg">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl font-bold mb-8 text-green-800">Plant Dashboard</h1>
      
      <!-- Search Bar -->
      <div class="mb-8">
        <input
          bind:value={searchQuery}
          type="text"
          placeholder="Search plants..."
          class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 focus:ring-green-500 bg-white"
        />
      </div>

      <!-- Display Plants -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        {#each plants as plant}
          <!-- svelte-ignore a11y-no-static-element-interactions -->
          <div
            class="bg-white p-6 rounded-lg shadow-md cursor-pointer hover:shadow-lg transition-all transform hover:scale-105"
            on:click={() => handlePlantClick(plant.id)}
          >
            <div class="flex items-center space-x-4">
              <div class="p-3 bg-green-100 rounded-full">
                <Leaf class="text-green-600" size={24} />
              </div>
              <div>
                <h3 class="text-xl font-semibold text-gray-800">{plant.name}</h3>
                <p class="text-gray-600">Click to view details</p>
              </div>
            </div>
          </div>
        {/each} <!-- ✅ Properly closed {#each} block -->
      </div>
    </div>
  </div>
</div>

