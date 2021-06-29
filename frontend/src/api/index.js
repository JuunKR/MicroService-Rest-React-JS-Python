import axios from 'axios'

const SERVER = 'http://127.0.0.1:8000/'



export const userSignup = signupRequest => axios.get(`${SERVER}member/signup`, signupRequest)
export const userLogin = loginRequest => axios.post(`${SERVER}member/login`, loginRequest)