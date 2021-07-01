import React from 'react'
import { Redirect, Route } from "react-router-dom"
import { MemberDelete, MemberDetail, MemberList, MemberModify, MemberRegister, MemberRetrieve, MemberLogin } from 'member'
import { PostDelete, PostDetail, PostList, PostModify, PostRegister, PostRetrieve } from 'board'
import { ItemDelete, ItemDetail, ItemList, ItemModify, ItemRegister, ItemRetrieve } from 'item'
import { Home, Member, Item, Board, Stock} from 'templates'
import { Nav } from 'common'
import { BrowserRouter as Router } from 'react-router-dom'

const App = () => {
  return (<div>
    <Router>
        <Nav/>
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'/home'}/>
        <Route exact path='/member' component={Member}/>
        <Route exact path='/member-delete' component={MemberDelete}/>
        <Route exact path='/member-detail' component={MemberDetail}/>
        <Route exact path='/member-list' component={MemberList}/>
        <Route exact path='/member-modify' component={MemberModify}/>
        <Route exact path='/member-register' component={MemberRegister}/>
        <Route exact path='/member-retrieve' component={MemberRetrieve}/>
        <Route exact path='/member-login' component={MemberLogin}/>
        <Route exact path='/item' component={Item}/>
        <Route exact path='/item-delete' component={ItemDelete}/>
        <Route exact path='/item-detail' component={ItemDetail}/>
        <Route exact path='/item-list' component={ItemList}/>
        <Route exact path='/item-modify' component={ItemModify}/>
        <Route exact path='/item-register' component={ItemRegister}/>
        <Route exact path='/item-retrieve' component={ItemRetrieve}/>
        <Route exact path='/board' component={Board}/>
        <Route exact path='/post-delete' component={PostDelete}/>
        <Route exact path='/post-detail' component={PostDetail}/>
        <Route exact path='/post-list' component={PostList}/>
        <Route exact path='/post-modify' component={PostModify}/>
        <Route exact path='/post-register' component={PostRegister}/>
        <Route exact path='/post-retrieve' component={PostRetrieve}/>
        <Route exact path='/stock' component={Stock}/>
    </Router>
  </div>)
}

export default App