// src/components/PokemonCard.js

import React, { useState } from 'react';
import './PokemonCard.css';

const PokemonCard = ({ pokemon }) => {
  const [expanded, setExpanded] = useState(false);

  const handleExpandClick = () => {
    setExpanded(true);
  };

  const handleCloseClick = () => {
    setExpanded(false);
  };

  return (
    <div className={`pokemon-card ${expanded ? 'expanded' : ''}`}>
      <button onClick={handleCloseClick}>Fechar</button>
      <img src={pokemon.image} alt={pokemon.name} className="pokemon-image" />
      <h3>{pokemon.name}</h3>
      {expanded && (
        <div className="pokemon-stats">
          <p>HP: {pokemon.stats?.hp}</p>
          <p>Attack: {pokemon.stats?.attack}</p>
          <p>Defense: {pokemon.stats?.defense}</p>
          <p>Special Attack: {pokemon.stats?.special_attack}</p>
          <p>Special Defense: {pokemon.stats?.special_defense}</p>
          <p>Speed: {pokemon.stats?.speed}</p>
        </div>
      )}
      {!expanded && <button onClick={handleExpandClick}>Expandir</button>}
    </div>
  );
};

export default PokemonCard;
