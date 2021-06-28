import React from 'react'
import { StockMenu as Menu } from '../common'
import './table.style.css'

const Stock = ({children}) => (<>
    <h1>Stock</h1>
    <Menu/>
    {children}
</>)

export default Stock