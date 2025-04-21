<script>
  export let id;
  import { Droplet, Thermometer, Beaker } from 'lucide-svelte';

  // Current NPK values
  let npkData = { nitrogen: 0, phosphorus: 0, potassium: 0 };

  // Generate random NPK values between 60–70
  function getRandomNPK() {
    return {
      nitrogen: Math.floor(Math.random() * 11) + 20,
      phosphorus: Math.floor(Math.random() * 11) + 20,
      potassium: Math.floor(Math.random() * 11) + 20
    };
  }

  // Regenerate NPK every 2 seconds
  setInterval(() => {
    npkData = getRandomNPK();
  }, 10000);

  // Sensor data from backend
  let sensorData = {
    temperature: 0,
    humidity: 0,
    soil_moisture: 0,
    npk: { nitrogen: 0, phosphorus: 0, potassium: 0 }
  };

  async function fetchSensorData() {
    try {
      const response = await fetch("http://192.168.206.245/data");
      if (!response.ok) throw new Error("Failed to fetch data");

      const data = await response.json();
      console.log("Fetched Sensor Data:", data);
      sensorData = { ...data };
    } catch (error) {
      console.error("Error fetching sensor data:", error);
    }
  }

  setInterval(fetchSensorData, 5000);

  const plantData = [
    {
      id: 1,
      name: "Tomato",
      requirements: {
        temperature: 25,
        soilmoisture: 72,
        npk: { nitrogen: 20, phosphorus: 20, potassium: 20 }
      }
    },
    {
      id: 2,
      name: "Cucumber",
      requirements: {
        temperature: 22,
        soilmoisture: 72,
        npk: { nitrogen: 10, phosphorus: 15, potassium: 20 }
      }
    },
    {
      id: 3,
      name: "Chilli",
      requirements: {
        temperature: 27,
        soilmoisture: 72,
        npk: { nitrogen: 15, phosphorus: 20, potassium: 25 }
      }
    }
  ];

  let isMotorRunning = false;
  let isLoading = false;

  $: selectedPlant = plantData.find(p => p.id === Number(id)) || plantData[0];

  async function toggleMotor() {
    isLoading = true;
    try {
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
                <p class="font-medium">{selectedPlant.requirements.soilmoisture}%</p>
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
                <p class="font-medium">{sensorData.soil_moisture}%</p>
              </div>
            </div>

            <div class="flex items-center space-x-4">
              <Beaker class="text-green-500" size={24} />
              <div>
                <p class="text-sm text-gray-600">NPK Levels</p>
                <p class="font-medium">
                  N: {npkData.nitrogen} |
                  P: {npkData.phosphorus} |
                  K: {npkData.potassium}
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
