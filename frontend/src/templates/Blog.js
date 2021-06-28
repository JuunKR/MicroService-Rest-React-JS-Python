import React from 'react'
import { BlogMenu as Menu } from '../common'
import './table.style.css'

const Blog = ({children}) => (<>
    <h1>Blog</h1>
    <Menu/>
    {children}
</>)

export default Blog