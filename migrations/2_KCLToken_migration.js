const KCLToken = artifacts.require("KCLToken");

module.exports = function (deployer) {
	deployer.deploy(KCLToken, 100000000000);
};
