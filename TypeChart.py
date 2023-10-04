superEffective = 2
inEffective = 0.5
effective = 1
immune = 0

fire = {
  'water':inEffective,
  'fire':inEffective,
  'ice':superEffective,
  'grass':superEffective,
  'flying':effective,
  'psychic':effective,
  'ground':effective,
  'rock':inEffective,
  'dark':effective,
  'fighting':effective,
  'fairy':effective,
  'ghost':effective,
  'dragon':inEffective,
  'steel':superEffective,
  'bug':superEffective,
  'electric':effective,
  'poison':effective,
  'normal':effective
}

water = {
  'water':inEffective,
  'fire':superEffective,
  'ice':effective,
  'grass':inEffective,
  'flying':effective,
  'psychic':effective,
  'ground':superEffective,
  'rock':superEffective,
  'dark':effective,
  'fighting':effective,
  'fairy':effective,
  'ghost':effective,
  'dragon':inEffective,
  'steel':effective,
  'bug':effective,
  'electric':effective,
  'poison':effective,
  'normal':effective
}

grass = {
  'water':superEffective,
  'fire':inEffective,
  'ice':effective,
  'grass':inEffective,
  'flying':inEffective,
  'psychic':effective,
  'ground':superEffective,
  'rock':superEffective,
  'dark':effective,
  'fighting':effective,
  'fairy':effective,
  'ghost':effective,
  'dragon':inEffective,
  'steel':inEffective,
  'bug':inEffective,
  'electric':effective,
  'poison':inEffective,
  'normal':effective
}

normal = {
  'water':effective,
  'fire':effective,
  'ice':effective,
  'grass':effective,
  'flying':effective,
  'psychic':effective,
  'ground':effective,
  'rock':inEffective,
  'dark':effective,
  'fighting':effective,
  'fairy':effective,
  'ghost':immune,
  'dragon':effective,
  'steel':inEffective,
  'bug':effective,
  'electric':effective,
  'poison':effective,
  'normal':effective
}

fighting = {
  'water':effective,
  'fire':effective,
  'ice':superEffective,
  'grass':effective,
  'flying':inEffective,
  'psychic':inEffective,
  'ground':effective,
  'rock':superEffective,
  'dark':superEffective,
  'fighting':effective,
  'fairy':inEffective,
  'ghost':immune,
  'dragon':effective,
  'steel':superEffective,
  'bug':inEffective,
  'electric':effective,
  'poison':effective,
  'normal':superEffective
}

ice = {
  'water':inEffective,
  'fire':inEffective,
  'ice':inEffective,
  'grass':superEffective,
  'flying':superEffective,
  'psychic':effective,
  'ground':superEffective,
  'rock':effective,
  'dark':effective,
  'fighting':effective,
  'fairy':effective,
  'ghost':effective,
  'dragon':superEffective,
  'steel':inEffective,
  'bug':effective,
  'electric':effective,
  'poison':effective,
  'normal':effective
}

ghost = {
  'water':effective,
  'fire':effective,
  'ice':effective,
  'grass':effective,
  'flying':effective,
  'psychic':superEffective,
  'ground':effective,
  'rock':effective,
  'dark':inEffective,
  'fighting':effective,
  'fairy':effective,
  'ghost':superEffective,
  'dragon':effective,
  'steel':effective,
  'bug':effective,
  'electric':effective,
  'poison':effective,
  'normal':immune
}

flying = {
  'water':effective,
  'fire':effective,
  'ice':effective,
  'grass':superEffective,
  'flying':effective,
  'psychic':effective,
  'ground':effective,
  'rock':inEffective,
  'dark':effective,
  'fighting':superEffective,
  'fairy':effective,
  'ghost':effective,
  'dragon':effective,
  'steel':inEffective,
  'bug':superEffective,
  'electric':inEffective,
  'poison':effective,
  'normal':effective
}

psychic = {
  'water':effective,
  'fire':effective,
  'ice':effective,
  'grass':effective,
  'flying':effective,
  'psychic':inEffective,
  'ground':effective,
  'rock':effective,
  'dark':immune,
  'fighting':superEffective,
  'fairy':effective,
  'ghost':effective,
  'dragon':effective,
  'steel':inEffective,
  'bug':effective,
  'electric':effective,
  'poison':superEffective,
  'normal':effective
}

ground = {
  'water':effective,
  'fire':superEffective,
  'ice':effective,
  'grass':inEffective,
  'flying':immune,
  'psychic':effective,
  'ground':effective,
  'rock':superEffective,
  'dark':effective,
  'fighting':effective,
  'fairy':effective,
  'ghost':effective,
  'dragon':effective,
  'steel':superEffective,
  'bug':inEffective,
  'electric':superEffective,
  'poison':superEffective,
  'normal':effective
}

rock = {
  'water':effective,
  'fire':superEffective,
  'ice':superEffective,
  'grass':effective,
  'flying':superEffective,
  'psychic':effective,
  'ground':effective,
  'rock':effective,
  'dark':effective,
  'fighting':effective,
  'fairy':effective,
  'ghost':effective,
  'dragon':superEffective,
  'steel':inEffective,
  'bug':superEffective,
  'electric':effective,
  'poison':effective,
  'normal':effective
}

fairy = {
  'water':effective,
  'fire':inEffective,
  'ice':effective,
  'grass':effective,
  'flying':effective,
  'psychic':effective,
  'ground':effective,
  'rock':effective,
  'dark':superEffective,
  'fighting':superEffective,
  'fairy':effective,
  'ghost':effective,
  'dragon':superEffective,
  'steel':inEffective,
  'bug':effective,
  'electric':effective,
  'poison':inEffective,
  'normal':effective
}

bug = {
  'water':effective,
  'fire':inEffective,
  'ice':effective,
  'grass':superEffective,
  'flying':inEffective,
  'psychic':superEffective,
  'ground':effective,
  'rock':inEffective,
  'dark':superEffective,
  'fighting':inEffective,
  'fairy':inEffective,
  'ghost':inEffective,
  'dragon':effective,
  'steel':inEffective,
  'bug':effective,
  'electric':effective,
  'poison':effective,
  'normal':effective
}

poison = {
  'water':effective,
  'fire':effective,
  'ice':effective,
  'grass':superEffective,
  'flying':effective,
  'psychic':effective,
  'ground':inEffective,
  'rock':inEffective,
  'dark':effective,
  'fighting':effective,
  'fairy':superEffective,
  'ghost':inEffective,
  'dragon':superEffective,
  'steel':immune,
  'bug':effective,
  'electric':effective,
  'poison':inEffective,
  'normal':effective
}

dragon = {
  'water':effective,
  'fire':effective,
  'ice':effective,
  'grass':effective,
  'flying':effective,
  'psychic':effective,
  'ground':effective,
  'rock':effective,
  'dark':effective,
  'fighting':effective,
  'fairy':immune,
  'ghost':effective,
  'dragon':superEffective,
  'steel':inEffective,
  'bug':effective,
  'electric':effective,
  'poison':effective,
  'normal':effective
}

electric = {
  'water':superEffective,
  'fire':effective,
  'ice':effective,
  'grass':inEffective,
  'flying':superEffective,
  'psychic':effective,
  'ground':immune,
  'rock':effective,
  'dark':effective,
  'fighting':effective,
  'fairy':effective,
  'ghost':effective,
  'dragon':inEffective,
  'steel':inEffective,
  'bug':effective,
  'electric':inEffective,
  'poison':effective,
  'normal':effective
}

dark = {
  'water':effective,
  'fire':effective,
  'ice':effective,
  'grass':effective,
  'flying':effective,
  'psychic':superEffective,
  'ground':effective,
  'rock':effective,
  'dark':inEffective,
  'fighting':inEffective,
  'fairy':inEffective,
  'ghost':superEffective,
  'dragon':effective,
  'steel':effective,
  'bug':effective,
  'electric':effective,
  'poison':effective,
  'normal':effective
}

steel = {
  'water':inEffective,
  'fire':inEffective,
  'ice':superEffective,
  'grass':effective,
  'flying':effective,
  'psychic':effective,
  'ground':effective,
  'rock':superEffective,
  'dark':effective,
  'fighting':effective,
  'fairy':superEffective,
  'ghost':effective,
  'dragon':effective,
  'steel':inEffective,
  'bug':effective,
  'electric':inEffective,
  'poison':effective,
  'normal':effective
}