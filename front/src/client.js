import { ApolloClient } from 'apollo-client'
import { HttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'

const client = new ApolloClient({
  link: new HttpLink({
    uri: 'http://localhost:5000/api/v1/graphql',
    fetchOptions: {
      // Might be unnecessary
      mode: 'cors'
    }
  }),
  cache: new InMemoryCache(),
})

export default client
