
import Button from '@mui/material/Button';
import DeleteIcon from '@mui/icons-material/Delete';

export default function MaterialUI () {
    
  let handleClicked = () => {
    console.log("button clicked");
  }

  return (
    <div>
      <h2>React</h2>
      <Button variant="contained" onClick={handleClicked}>Click me</Button>
      {/* <Button variant="outlined" startIcon={<DeleteIcon />}>
        Delete
      </Button> */}
      <Button variant="contained" onClick={handleClicked} color='success' size="small"  startIcon={<DeleteIcon/>}>Click me 9</Button>
    </div>
  )
}