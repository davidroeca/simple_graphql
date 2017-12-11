import React from 'react'
import { render } from 'react-dom'
import { ApolloProvider } from 'react-apollo'
import './index.css'
import App from './App'
import client from './client'
import registerServiceWorker from './registerServiceWorker'

render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>,
  document.getElementById('root')
)

registerServiceWorker()
