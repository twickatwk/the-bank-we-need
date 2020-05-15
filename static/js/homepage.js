
// This is the main component for the page
class Page extends React.Component {
    render() {
        return (
            <div class="container">
                <div class="row">
                    <div class="col">
                        <h4>Welcome to THE BANK</h4>
                    </div>
                </div>
            </div>
        )
    }
}

ReactDOM.render(
    <Page />,
    document.getElementById('root')
);