async addPost() {
   if(
    this.state.caption
) {
    let postData = {
        preview_image: this.state.previewImage,
        caption: this.state.caption,
        author: firebase.auth().currentUser.displayName,
        created on: new Date(),
        author uid: firebase.auth () . currentUser.uid,
        profile_image: this.state.profile_image, 
        likes: 0
};
await firebase 
  .database ()
 .ref (
    "/posts/" +
    Math. random ()
       .toString (36)
       .slice (2)
 )
 .set (postData)
 .then (function (snapshot) { }) ;
this.props.setUpdateToTrue () ;
this.props.navigation.navigate ("Feed");
} else {
   Alert.alert (
   "Error"
   "All fields are required!"
  [f text: "OK", onPress: () => console. log ("OK Pressed") }], {
   );
  }
}

constructor (props) {
   super (props) ;
    this.state = {
      light theme: true,
      post_id: this.props.post.key, 
      post data: this.props.post. value
  };
}