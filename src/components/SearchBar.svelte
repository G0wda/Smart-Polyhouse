<script>
    import { onMount } from "svelte";
    import { writable } from "svelte/store";
    import SearchIcon from "lucide-svelte/icons/search";
  
    // Reactive value store
    export let value = "";
    export let onChange = (v) => {};
  
    function handleInput(event) {
      value = event.target.value;
      onChange(value);
    }
  </script>
  
  <div class="relative w-full max-w-xl">
    <SearchIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size="20" />
    <input
      type="text"
      bind:value={value}
      on:input={handleInput}
      placeholder="Search plants..."
      class="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
    />
  </div>
  