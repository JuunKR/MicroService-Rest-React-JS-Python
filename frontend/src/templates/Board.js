import React from 'react'
import { BoardMenu as Menu } from '../common'
import './table.style.css'

const Board = ({children}) => (<>
    <h1>Board</h1>
    <Menu/>
    {children}
</>)

export default Board