import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
// import { Table,TableBody,TableCell, TableContainer, TableHead, TableRow, Paper,} from "@material-ui/core";
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import {TableFooter} from '@material-ui/core';
import {TablePagination} from '@material-ui/core';
import Pagination from '@material-ui/lab/Pagination'
import faker from "faker/locale/ko";

import  {memberList}  from 'api'



const useStyles = makeStyles({
  table: {
    minWidth: 650,
  },

});
const usePageStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      marginTop: theme.spacing(2),

    },
  },
}));


const MemberList = () => {

  faker.seed(123);

  const users = Array(53)
  .fill()
  .map(() => ({
    id: faker.random.uuid(),
    name: faker.name.lastName() + faker.name.firstName(),
    email: faker.internet.email(),
    phone: faker.phone.phoneNumber()
  }));

  const UserTable = () => {
    const [page, setPage] = useState(0)
    const [rowsPerPage, setRowsPerPage] = useState(10)
  
    const handleChangePage = (event, newPage) => {
      setPage(newPage)
    }
  
    const handleChangeRowsPerPage = (event) => {
      setRowsPerPage(parseInt(event.target.value, 10))
      setPage(0)
    }

    return (
      <TableContainer component={Paper}>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>No</TableCell>
            <TableCell align="right">Name</TableCell>
            <TableCell align="right">Email</TableCell>
            <TableCell align="right">Phone</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {users
            .slice(page * rowsPerPage, (page + 1) * rowsPerPage)
            .map(({ id, name, email, phone }, i) => (
              <TableRow key={id}>
                <TableCell component="th" scope="row">
                  {page * rowsPerPage + i + 1}
                </TableCell>
                <TableCell align="right">{name}</TableCell>
                <TableCell align="right">{email}</TableCell>
                <TableCell align="right">{phone}</TableCell>
              </TableRow>
            ))}
        </TableBody>
        <TableFooter>
          <TableRow>
            <TablePagination
              count={users.length}
              page={page}
              rowsPerPage={rowsPerPage}
              onChangePage={handleChangePage}
              onChangeRowsPerPage={handleChangeRowsPerPage}
            />
          </TableRow>
        </TableFooter>
      </Table>
    </TableContainer>
    )

  }

  const [members, setMembers] = useState([])

  const classes = useStyles();
  const pageClasses = usePageStyles();


  useEffect(() => {
    memberList()
      .then(res => {
        // alert(typeof(JSON.stringify(res.data)))
        setMembers(res.data)
      })
      .catch(err => {
        console.log(err.data)
      })

  }, [])

  return (<>
    {UserTable}
    <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>회원 ID</TableCell>
            <TableCell align="right">비밀번호</TableCell>
            <TableCell align="right">회원 이름</TableCell>
            <TableCell align="right">이메일</TableCell>
          </TableRow>
        </TableHead>

        <TableBody>

          {members.length != 0
            ? members.map((member) => (
              <TableRow key={member.username}>
                <TableCell align="right">{member.username}</TableCell>
                <TableCell component="th" scope="row">{member.password}</TableCell>
                <TableCell align="right">{member.name}</TableCell>
                <TableCell align="right">{member.email}</TableCell>
              </TableRow>)
            )
            : <TableRow>
              <TableCell component="th" scope="row" colSpan="4">
                <h1>등록된 데이터가 없습니다</h1>
              </TableCell>

            </TableRow>
          }
        </TableBody>
      </Table>
    </TableContainer>
    <div className={pageClasses.root}>
      <Pagination count={10} color="primary" />
    </div>
  </>);
}

export default MemberList

/*
 <TableRow key={row.name}>
    <TableCell component="th" scope="row">
    {row.name}
    </TableCell>
    <TableCell align="right">{row.calories}</TableCell>
    <TableCell align="right">{row.fat}</TableCell>
    <TableCell align="right">{row.carbs}</TableCell>
</TableRow>
*/