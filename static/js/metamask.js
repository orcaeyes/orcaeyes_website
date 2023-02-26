class MetaMask {
    constructor() {
        this.btn_connect = $("#btn_metamask_connect");
        this.events();
    }

    events() {
        this.btn_connect.click(function() {
            ethereum.request({ method: 'eth_requestAccounts' });
        });
    }
}

$( document ).ready(function() {
    var mm = new MetaMask();
});