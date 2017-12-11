import React from 'react'
import { graphql, compose } from 'react-apollo'
import gql from 'graphql-tag'

const FORM_STATE_QUERY = gql`
query getFormState {
  formState {
    sections {
      name,
      fields {
        name,
        fieldName,
        options {
          label,
          value
        }
      }
    }
  }
}
`

const FORM_SUBMISSION = gql`
mutation submitForm {
  submission(
    subject: $subject,
    body: $body,
    authorEmail: $authorEmail
  ) {
    ok
  }
}
`

const Form = ({ data, formSubmission }) => {
  const { formState, refetch } = data
  return (
    <form onSubmit={() => formSubmission('Hey', 'Yooo', 'sandy@gmail.com')}>
      <button onClick={() => refetch()}>
        Refresh
      </button>
      {formState && formState.sections && formState.sections.map(section => (
        <div>
          <h1>{section.name}</h1>
          <div>
            {section.fields && section.fields.map(field => (
              <div>
                {field && (
                  field.options ? (
                    <select>
                      {field.options.map(option => (
                        <option value={option.value}>{option.label}</option>
                      ))}
                    </select>
                  ) : (
                    <div>
                      <label>
                        {field.name}
                        <input type="text" name={field.fieldName} />
                      </label>
                    </div>
                  )
                )}
              </div>
            ))}
          </div>
        </div>
      ))}
      <input type="submit" /><br/>
    </form>
  )
}

export default compose(
  graphql(FORM_STATE_QUERY, { name: 'data' }),
  graphql(FORM_SUBMISSION, { name: 'formSubmission' }),
)(Form)
