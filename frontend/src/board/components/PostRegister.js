import React,{useImperativeHandle, useState} from 'react'
import '../styles/PostRegister.css'
import { Button } from '@material-ui/core';
import { useHistory } from 'react-router-dom';
import { postRegister } from 'api'

const PostRegister = () => {
  const history = useHistory()
  const [postInfo, setPostInfo] = useState({
    title: '',
    content: ''
  })

  const {title, content} = 'postInfo'

  const handleSubmit = e => {
    e.preventDefault()
    let handleErrors = response => {
      if (!response.ok) {
        throw Error(response.statusText);
      }
      return response;
    }
    alert(`작성하시겠습니까?: ${JSON.stringify({...postInfo})}`)
    postRegister({...postInfo})
    .then(res => {
      alert(`작성 완료 : ${res.data.result} `)
      // history.push('login')
      
    })
    .catch(err => {
      alert(`작성 실패 : ${err}`)
    })
  }

  const handleClick = e => {
    e.preventDefault()
    alert('취소 클릭')
  }

  const handleChange = e => {
    const { name, value } = e.target
    setPostInfo({
      ...postInfo,
      [name]: value
    })

  }



    return (<>
    <div className="Signup">
    <form onSubmit={handleSubmit} method="post" style={{border:"1px solid #ccc"}}>
      <div className="container">
        <h1>게시글 쓰기</h1>
        <p>Please fill in this form to create an account.</p>
        <hr/>
        <label for="title"><b>title</b></label>
        <input type="text" placeholder="Enter title" onChange={handleChange}   name="title" value={title}/>
        <label for="content"><b>content</b></label>
        <input type="text" placeholder="Enter content" onChange={handleChange}  name="content" value={content} />
        <div class="clearfix">
          <button type="submit" className="signupbtn">Register</button>
          <button type="button" className="cancelbtn" onClick={handleClick}>Cancel</button>
          
        </div>
      </div>
  </form>
</div>
</>)
}

export default PostRegister