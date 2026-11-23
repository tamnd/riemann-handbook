---
id: loc-tau
title: The lowering derivative of the vacuum is a sum of singular test operators
kind: theorem
decl: PositivityTheory.Rg.Sw.HSt.locTau
module: Development.WeilBound.RepresentationTheoryGL.SiegelWeilProof.HolomorphicContinuation.CayleyCosetSums.LocTau
covers: 308
status: drafted
drafted_by: writer@claude
---
This theorem proves `LocTau`, a local fact about the group $U(n,n)$. It is one of the three inputs of [`holLeadB`](/proof/siegel-weil/), which shows that the Eisenstein series has no pole at $s_0$ when $m<n$. It says that one derivative of the vacuum section can be written with test operators whose test functions are singular. The proof only puts four facts together; three of them are local computations and the fourth, `crux`, is a nonvanishing statement.

## Statement

Let $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ in $M_{2n}(\mathbb{C})$. Let $G$ be the group of $g$ with $g^{*}Jg=J$, and let $K$ be the subgroup of unitary $g\in G$. For $g=(g_{ij})$ in blocks, put $u_1(g)=i g_{21}+g_{22}$. The vacuum section is

$$f_z(x)=\det(x)^{e}\,\det u_1(x)^{-m}\,\bigl(\det u_1(x)\det \bar u_1(x)\bigr)^{-z},$$

where $\bar u_1(x)=(x^{-1})_{11}+i(x^{-1})_{21}$. For $Q\in M_n(\mathbb{C})$, let $L_Q$ be the complexified right derivative along the lowering element $C\begin{pmatrix}1&Q\\0&1\end{pmatrix}C^{-1}-1$, with $C$ the Cayley matrix. A *singular test* is a continuous function $\psi$ with compact support on real $n\times n$ matrices whose Fourier transform vanishes at every singular Hermitian $\beta$. For such $\psi$, a continuous $\rho$ on $K$ and $a,b\in G$, the test operator is

$$T_{\rho,\psi,a,b}F(x)=\int_K \rho(k)\int F\bigl(x\,k\,a\,n(t)\,b\bigr)\,\psi(t)\,dt\,dk,$$

with $n(t)$ the unipotent element of the Hermitian matrix built from $t$.

**Theorem.** Let $m<n$, $e\in\mathbb{Z}$ and $Q\in M_n(\mathbb{C})$. There are $N$, singular tests $\psi_l$, continuous $\rho_l$, elements $a_l,b_l\in G$, an entire $D$ with $D(0)\neq0$ and entire $M_l$ such that for all $z\in\mathbb{C}$ and $x\in G$

$$D(z)\,L_Q f_z(x)=\sum_{l=1}^{N} M_l(z)\,T_{\rho_l,\psi_l,a_l,b_l}f_z(x).$$

## Proof

The four facts are these. `lt1`: $L_Q f_z = z\,e_Q(z)$, where $e_Q(z)=f_z\cdot\operatorname{tr}(\Omega Q)$ for a fixed matrix function $\Omega$. `lt2`: for a continuous $\psi$ with compact support and $a,b\in G$, there is one entire $c$ such that $T_{\rho_Y,\psi,a,b}f_z=c(z)\,e_{Y^{*}}(z)$ for every $Y\in M_n(\mathbb{C})$. Here $\rho_Y$ is a fixed function on $K$ built from $Y$ and $f_0$. `lt3`: for $m<n$ and a singular test $\psi$, $T_{\rho,\psi,a,b}f_0=0$. `crux`: some $T_{\rho_P,\psi,a,b}f_z(x_0)$ has a nonzero derivative at $z=0$.

1. Take $P,\psi,a,b,x_0$ from `crux` and $c$ from `lt2`.
2. Apply `lt3` and `lt2` at $x=1$ with $Y=1$. Since $e_1(0)(1)=-\operatorname{tr}1=-n$, this gives $c(0)\,n=0$. As $n>m\ge0$, $c(0)=0$.
3. Then the derivative at $0$ in `crux` is $c'(0)$ times a value of $e_{P^{*}}(0)$. So $c'(0)\neq0$. The Lean proof treats the case of a zero base of the power $(\cdot)^{-z}$ apart.
4. Put $D(z)=c(z)/z$, so $D(0)=c'(0)\neq0$. Take $N=1$, $M_1=1$ and $\rho_1=\rho_{Q^{*}}$. By `lt1` and `lt2`, $D(z)L_Qf_z=c(z)e_Q(z)=T_{\rho_1,\psi,a,b}f_z$.

## In the Lean code

The theorem is in [LocTau.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/CayleyCosetSums/LocTau.lean#L9). Its proof is `asmLT lt1 lt2 lt3 crux`.

- `LocTau`, `fz`, `rC`, `lowQ` and `tOp` are in [LocTauAlt.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/CayleyCosetSums/LocTauAlt.lean#L33). The statement quantifies over every compact group with a Haar measure and a continuous map onto $K$, not over $K$ itself.
- The four statements and `AsmLT` are in [MultiplicityOneTestOperatorsAlt.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/CayleyCosetSums/MultiplicityOneTestOperatorsAlt.lean#L22). There $\rho_Y$ is `rhoP` and $e_Q$ is `eQ`.
- `asmLT` is in [DetSecondCayleyBlockNe.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/CayleyCosetSums/DetSecondCayleyBlockNe.lean#L154). It takes $D$ as `dslope c 0`.
- `IsSingTest`, `herm` and `nU` are in [IsSingTest.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/IsSingTest.lean#L33).
- `lt1` is in [LoweringDerivativeVacuum.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/CayleyCosetSums/LoweringDerivativeVacuum.lean#L68), `lt2` in [LamTrace.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/CayleyCosetSums/LamTrace.lean#L110), `lt3` in [SingularTestsKillVacuum.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/CayleyCosetSums/SingularTestsKillVacuum.lean#L11) and `crux` in [Crux.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/CayleyCosetSums/Crux.lean#L11). I have not unfolded their proofs.

`lt1`, `lt2` and `asmLT` each have two declarations with the same name in different namespaces; the second is an alias of the first.
