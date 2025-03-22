<script>
  export let id; // Plant ID passed as a prop
  import { Droplet, Thermometer, Beaker } from 'lucide-svelte';

  // Mock plant data - replace with actual API calls
  const plantData = [
    {
      id: 1,
      name: "Tomato",
      requirements: {
        temperature: 25,
        moisture: 60,
        npk: { nitrogen: 20, phosphorus: 20, potassium: 20 }
      }
    },
    {
      id: 2,
      name: "Cucumber",
      requirements: {
        temperature: 22,
        moisture: 55,
        npk: { nitrogen: 10, phosphorus: 15, potassium: 20 }
      }
    },
    {
      id: 3,
      name: "Chilli",
      requirements: {
        temperature: 27,
        moisture: 50,
        npk: { nitrogen: 15, phosphorus: 20, potassium: 25 }
      }
    }
  ];
  let soilMoisture = 0;

  async function fetchSoilMoisture() {
    try {
      const response = await fetch("http://192.168.211.245/soilmoisture");
      const data = await response.json();
      soilMoisture = data.moisture;
    } catch (error) {
      console.error("Error fetching soil moisture:", error);
    }
  }

  setInterval(fetchSoilMoisture, 5000); // Fetch data every 5 sec

  // Default sensor readings (Replace with API data)
  let sensorData = {
    temperature: 23,
    moisture: 45,
    npk: { nitrogen: 10, phosphorus: 18, potassium: 18 }
  };

  let isMotorRunning = false;
  let isLoading = false;

  // Find the correct plant by ID
  $: selectedPlant = plantData.find(p => p.id === Number(id)) || plantData[0];

  // Determine if the motor should be turned on based on moisture level
  $: motorShouldBeOn = sensorData.moisture < selectedPlant.requirements.moisture;

  async function toggleMotor() {
    isLoading = true;
    try {
      // Simulate API delay
      await new Promise(resolve => setTimeout(resolve, 500));
      isMotorRunning = !isMotorRunning;
      console.log(`Motor turned ${isMotorRunning ? 'on' : 'off'}`);
    } catch (error) {
      console.error('Error toggling motor:', error);
      alert('Failed to toggle motor. Please try again.');
    } finally {
      isLoading = false;
    }
  }
</script>

<div class="min-h-screen bg-[url('https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?auto=format&fit=crop&q=80')] bg-cover bg-center bg-fixed">
  <div class="max-w-4xl mx-auto p-6">
    <div class="bg-white/90 rounded-lg shadow-lg p-6 backdrop-blur-sm">
      <h2 class="text-3xl font-bold text-gray-800 mb-6">{selectedPlant.name}</h2>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Required Conditions -->
        <div class="space-y-6">
          <h3 class="text-xl font-semibold text-gray-700">Required Conditions</h3>
          <div class="space-y-4">
            <div class="flex items-center space-x-4">
              <Thermometer class="text-red-500" size={24} />
              <div>
                <p class="text-sm text-gray-600">Temperature</p>
                <p class="font-medium">{selectedPlant.requirements.temperature}°C</p>
              </div>
            </div>

            <div class="flex items-center space-x-4">
              <Droplet class="text-blue-500" size={24} />
              <div>
                <p class="text-sm text-gray-600">Soil Moisture</p>
                <p class="font-medium">{selectedPlant.requirements.moisture}%</p>
              </div>
            </div>

            <div class="flex items-center space-x-4">
              <Beaker class="text-green-500" size={24} />
              <div>
                <p class="text-sm text-gray-600">NPK Levels</p>
                <p class="font-medium">
                  N: {selectedPlant.requirements.npk.nitrogen} | 
                  P: {selectedPlant.requirements.npk.phosphorus} | 
                  K: {selectedPlant.requirements.npk.potassium}
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Current Readings -->
        <div class="space-y-6">
          <h3 class="text-xl font-semibold text-gray-700">Current Readings</h3>
          <div class="space-y-4">
            <div class="flex items-center space-x-4">
              <Thermometer class="text-red-500" size={24} />
              <div>
                <p class="text-sm text-gray-600">Temperature</p>
                <p class="font-medium">{sensorData.temperature}°C</p>
              </div>
            </div>

            <div class="flex items-center space-x-4">
              <Droplet class="text-blue-500" size={24} />
              <div>
                <p class="text-sm text-gray-600">Soil Moisture</p>
                <p class="font-medium">{soilMoisture}%</p>
              </div>
            </div>

            <div class="flex items-center space-x-4">
              <Beaker class="text-green-500" size={24} />
              <div>
                <p class="text-sm text-gray-600">NPK Levels</p>
                <p class="font-medium">
                  N: {sensorData.npk.nitrogen} | 
                  P: {sensorData.npk.phosphorus} | 
                  K: {sensorData.npk.potassium}
                </p>
              </div>
            </div>
          </div>

          <!-- Motor Toggle Button -->
          <button
            on:click={toggleMotor}
            class="w-full px-4 py-2 rounded-lg text-white transition-all 
                   {isMotorRunning ? 'bg-red-500 hover:bg-red-600' : 'bg-green-500 hover:bg-green-600'}"
            disabled={isLoading}
          >
            {isLoading ? 'Processing...' : (isMotorRunning ? 'Turn Motor Off' : 'Turn Motor On')}
          </button>
        </div>
      </div>
    </div>
  </div>
</div>
