{
  description = "sort shadowplay files after date";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:


    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system};
      in
      rec {

        # Use nixpkgs-fmt for `nix fmt'
        formatter = pkgs.nixpkgs-fmt;

        defaultPackage = packages.shadowplay-sort;
        packages = flake-utils.lib.flattenTree rec {

          shadowplay-sort = with pkgs.python3Packages;
            pkgs.python3Packages.buildPythonPackage rec {
              pname = "shadowplay-sort";
              version = "1.0.0";
              propagatedBuildInputs = [ setuptools ];
              doCheck = false;
              src = self;
              meta = with pkgs.lib; {
                description = "sort shadowplay files after date";
                homepage = "https://github.com/MayNiklas/shadowplay-sort/";
                platforms = platforms.unix;
                maintainers = with maintainers; [ mayniklas ];
              };
            };

        };


      });
}
