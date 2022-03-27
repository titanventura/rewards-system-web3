const RewardsSystem = artifacts.require("RewardsSystem");

module.exports = function (deployer) {
	deployer.deploy(RewardsSystem);
};
