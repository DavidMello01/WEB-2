// src/App.js

import React from 'react';
import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client';
import PokemonList from './components/PokemonList';

const client = new ApolloClient({
  uri: 'https://graphql-pokemon2.vercel.app/',
  cache: new InMemoryCache()
});

function App() {
  return (
    <ApolloProvider client={client}>
      <div className="App">
        <header className="App-header">
          <h1>Listinha Pokemon</h1>
        </header>
        <PokemonList />
      </div>
    </ApolloProvider>
  );
}

export default App;
