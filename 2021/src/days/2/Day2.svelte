<script>
  import { _sample, _input } from "./input.js";

  const input = _input.split("\n").map((v) => {
    v = v.split(" ");
    v[1] = Number(v[1]);
    return v;
  });

  const part1 = () => {
    let x = 0;
    let depth = 0;
    input.forEach((el) => {
      const [direction, units] = el;
      if (direction === "forward") x += units;
      else depth += direction === "up" ? -units : units;
    });
    return depth * x;
  };

  const part2 = () => {
    let x = 0;
    let depth = 0;
    let aim = 0;
    input.forEach((el) => {
      const [direction, units] = el;
      if (direction === "forward") {
        x += units;
        depth += aim * units;
      } else aim += direction === "up" ? -units : units;
    });
    return depth * x;
  };
</script>

<div class="vertical">
  <code>{part1()}</code>
  <code>{part2()}</code>
</div>
