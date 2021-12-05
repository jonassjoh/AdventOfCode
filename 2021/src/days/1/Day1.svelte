<script>
  import { prevent_default } from "svelte/internal";

  import { _sample, _input } from "./input.js";

  const input = _input.split("\n").map(Number);

  const part1 = (res) => {
    return res.reduce((acc, _, i, arr) => acc + (arr[i - 1] < arr[i]), 0);
  };

  const part2 = (edgeSize = 1) => {
    const res = input.map((_, i, arr) => {
      return arr
        .slice(i - edgeSize, i + edgeSize + 1)
        .reduce((acc, _, __, arr) => arr, undefined)
        ?.reduce((acc, v) => acc + v);
    }, 0);
    return part1(res);
  };
</script>

<div class="vertical">
  <code>{part1(input)}</code>
  <code>{part2()}</code>
</div>
