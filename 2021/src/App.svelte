<script>
  import { Router, Link, Route } from "svelte-navigator";
  import Day1 from "./days/1/Day1.svelte";
  import Day2 from "./days/2/Day2.svelte";
</script>

<main>
  <Router>
    <Link to="/"><h1>Advent of Code 2021</h1></Link>

    <Route path="/">
      <nav>
        <Link to="day1">
          <div class="card">1</div>
        </Link>
        <Link to="day2">
          <div class="card">2</div>
        </Link>
        <Link to="day3">
          <div class="card">3</div>
        </Link>
        <Link to="day4">
          <div class="card">4</div>
        </Link>
        <Link to="day5">
          <div class="card">5</div>
        </Link>
        <Link to="day6">
          <div class="card">6</div>
        </Link>
        <Link to="day7">
          <div class="card">7</div>
        </Link>
        <Link to="day8">
          <div class="card">8</div>
        </Link>
        <Link to="day9">
          <div class="card">9</div>
        </Link>
        <Link to="day10">
          <div class="card">10</div>
        </Link>
        <Link to="day11">
          <div class="card">11</div>
        </Link>
        <Link to="day12">
          <div class="card">12</div>
        </Link>
        <Link to="day13">
          <div class="card">13</div>
        </Link>
        <Link to="day14">
          <div class="card">14</div>
        </Link>
        <Link to="day15">
          <div class="card">15</div>
        </Link>
        <Link to="day16">
          <div class="card">16</div>
        </Link>
        <Link to="day17">
          <div class="card">17</div>
        </Link>
        <Link to="day18">
          <div class="card">18</div>
        </Link>
        <Link to="day19">
          <div class="card">19</div>
        </Link>
        <Link to="day20">
          <div class="card">20</div>
        </Link>
        <Link to="day21">
          <div class="card">21</div>
        </Link>
        <Link to="day22">
          <div class="card">22</div>
        </Link>
        <Link to="day23">
          <div class="card">23</div>
        </Link>
        <Link to="day24">
          <div class="card">24</div>
        </Link>
      </nav>
    </Route>
    <Route path="day1" component={Day1} />
    <Route path="day2" component={Day2} />
  </Router>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  nav {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 20px;
  }

  nav .card {
    background-color: #ff3e00;
    width: 100%;
    aspect-ratio: 1;
    font-size: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fafafa;
    user-select: none;
    transition: all 0.1s ease;
    border-radius: 10px;
  }

  nav .card:hover {
    font-size: 70px;
    border-radius: 40px;
  }
</style>
