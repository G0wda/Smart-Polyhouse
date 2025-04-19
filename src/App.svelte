<script>
  import { Router, Link, Route } from "svelte-routing";
  import Home from "./routes/Home.svelte";
  import Login from "./routes/Login.svelte";
  import Dashboard from "./routes/Dashboard.svelte";
  import PlantDetails from "./routes/PlantDetails.svelte";
    import Register from "./routes/Register.svelte";
  
  export let url = "";
</script>

<Router {url}>
  <main class="min-h-screen bg-gray-100">
    <Route path="/" component={Home} />
    <Route path="/login" component={Login} />
    <Route path="/dashboard" component={Dashboard} />
    <Route path="/plant/:id" component={PlantDetails} />
    <Route path="/register" component={Register}/>
  </main>
</Router>