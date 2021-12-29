import api from '@/services/api'

export default {
  getContacts() {
    return api.get(`contacts/`)
              .then(response => response.data)
  },
  addContact(payload) {
    return api.post(`contacts/add/`, payload)
              .then(response => response.data)
  },
}