pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";

contract KCLToken is ERC20Burnable {
    address public owner;

    constructor(uint256 initialSupply) ERC20("KCT CodeLabs", "KCL") {
        _mint(msg.sender, initialSupply);
        owner = msg.sender;
    }

    function mint(address user, uint256 amount) public {
        require(msg.sender == owner, "Only the owner can mint tokens.");

        _mint(user, amount);
    }

    function decimals() public view virtual override returns (uint8) {
        return 0;
    }
}
