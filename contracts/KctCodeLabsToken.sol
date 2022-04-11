pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract KCLToken is ERC20 {
    address public owner;

    constructor(uint256 initialSupply) ERC20("KCT CodeLabs", "KCL") {
        _mint(msg.sender, initialSupply);
        owner = msg.sender;
    }

    function mint(uint256 amount) public {
        require(msg.sender == owner, "Only the owner can mint tokens.");

        _mint(owner, amount);
    }

    function decimals() public view virtual override returns (uint8) {
        return 0;
    }
}
