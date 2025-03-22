

<script>
    import { navigate } from "svelte-routing";
    
    let searchQuery = "";
    let plants = [];
    
    const mockPlants = [
      { id: 1, name: "Tomato", temp: 25, moisture: 60, npk: "20-20-20" },
      { id: 2, name: "Cucumber", temp: 23, moisture: 65, npk: "15-15-15" },
      { id: 3, name: "Lettuce", temp: 20, moisture: 70, npk: "10-10-10" }
    ];


    const handlePlantClick = (id) => {
    navigate(`/plant/${id}`);
  };
</script>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    {#each plants as plant}
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <div
        class="bg-white p-6 rounded-lg shadow-md cursor-pointer hover:shadow-lg transition-shadow"
        on:click={() => handlePlantClick(plant.id)}
      >
        <h3 class="text-xl font-semibold mb-2">{plant.name}</h3>
        <p class="text-gray-600">Click for details</p>
      </div>
    {/each}
</div>