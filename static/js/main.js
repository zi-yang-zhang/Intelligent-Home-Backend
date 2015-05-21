var Main = React.createClass({
    render: function(){
        return (
            <div className="main">
                <h1> Test!</h1>
            </div>
        )

    }
});
React.render(
  <Main />,
  document.getElementById('content')
);