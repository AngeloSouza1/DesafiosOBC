function navigateElf(steps) {
  let position = { x: 0, y: 0 };
  
  for (let step of steps) {
    switch (step) {
      case "UP":
        if (position.y > 0) position.y -= 1;
        break;
      case "DOWN":
        if (position.y < 9) position.y += 1;
        break;
      case "LEFT":
        if (position.x > 0) position.x -= 1;
        break;
      case "RIGHT":
        if (position.x < 9) position.x += 1;
        break;
      default:
        break;
    }
  }

  return position;
}


console.log(navigateElf(["RIGHT", "RIGHT", "UP", "DOWN", "LEFT", "UP"]));
