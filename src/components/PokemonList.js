import React, { useState } from 'react';
import { useQuery, gql } from '@apollo/client';
import './PokemonList.css'; // Importe o arquivo CSS
import PokemonCard from './PokemonCard'; // Importe o componente PokemonCard

const GET_POKEMONS = gql`
  query {
    pokemons(first: 10) {
      id
      name
      image
    }
  }
`;

const PokemonList = () => {
  const { loading, error, data } = useQuery(GET_POKEMONS);
  const [selectedPokemon, setSelectedPokemon] = useState(null);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  const handlePokemonClick = (pokemon) => {
    setSelectedPokemon(pokemon);
  };

  return (
    <div>
      <h2>Pokemons</h2>
      <ul className="pokemon-list">
        {data.pokemons.map(pokemon => (
          <li key={pokemon.id} className="pokemon-item" onClick={() => handlePokemonClick(pokemon)}>
            {pokemon.name}
          </li>
        ))}
      </ul>
      {selectedPokemon && <PokemonCard pokemon={selectedPokemon} />}
    </div>
  );
};

export default PokemonList;
