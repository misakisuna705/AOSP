//
// Copyright (C) 2003 Andras Varga; CTIE, Monash University, Australia
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public License
// as published by the Free Software Foundation; either version 2
// of the License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with this program; if not, see <http://www.gnu.org/licenses/>.
//


//
// Server side of the EtherCli model -- generates EtherAppResp packets
// with the number of bytes requested by the client in EtherAppReq.
// It should be connected directly to EtherLLC or a Ieee802NicXXX module.
//
simple EtherAppSrv
{
    parameters:
        bool registerSAP; // whether to sent IEEE802CTRL_REGISTER_DSAP on startup
    gates:
        input in;
        output out;
}
