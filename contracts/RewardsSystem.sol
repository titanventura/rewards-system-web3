// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract RewardsSystem {
    mapping(address => uint256) public balanceOf;
    address public webAppController = msg.sender;

    function increaseAsset(address user, uint256 amount) public returns (bool) {
        // require(msg.sender == webAppController, "Invalid access");
        balanceOf[user] += amount;
        return true;
    }

    function decreaseAsset(address user, uint256 amount) public returns (bool) {
        // require(msg.sender == webAppController, "Invalid access");
        require(
            balanceOf[user] >= amount,
            "Decrease amount greater than balance"
        );
        balanceOf[user] -= amount;
        return true;
    }

    function transferAsset(
        address from,
        address to,
        uint256 amount
    ) public returns (bool) {
        // require(msg.sender == webAppController, "Invalid access");
        decreaseAsset(from, amount);
        increaseAsset(to, amount);
        return true;
    }

    function getBalancesOfAll(address[] memory users)
        public
        returns (uint256[] memory)
    {
        // require(msg.sender == webAppController, "Invalid access");
        uint256[] memory amounts = new uint256[](users.length);

        for (uint256 i = 0; i < users.length; i++) {
            amounts[i] = balanceOf[users[i]];
        }

        return amounts;
    }
}
