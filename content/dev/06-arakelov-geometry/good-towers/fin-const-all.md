---
id: fin-const-all
title: The p-adic norm of a flat frame function is constant
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Flat.FinAll.finConstAll
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.FiniteConstantAllHolds
covers: 430
status: drafted
drafted_by: writer@claude
---
This theorem proves `FinConstAll`: if a frame function is flat on a model over a $p$-adic discrete valuation ring, then its $p$-adic log norm at integral frames is one constant. Its statement form is [`finite_constant_all_holds`](/entry/finite-constant-all-holds/). The last step is [`value_at_point`](/entry/value-at-point/), through its statement form [`eigen_line_p_adic_frame`](/entry/eigen-line-p-adic-frame/).

## Statement

Let $E$ be a CM field with host datum $H$, $D$ a datum of signature $(p, q)$, $X^\circ$ the moduli space at a level, $F$ a coefficient field, $\tau \colon E \to \mathbb{C}$ with $\tau(\sqrt{-d}) = \mathrm{rt}_0$, $\ell$ a prime and $\kappa \colon F \to \mathbb{C}_\ell$. Let $O$ be a discrete valuation ring and $\beta \colon O \to F$ injective with $\beta(O) = \{x : |\kappa x| \le 1\}$. Let $Y$ be a model of $X^\circ$ over $O$ with `SplitFibres` and `N3`, $U$ a set of points of $X^\circ_F$, and $Z$ a `CptOver Y U`: a point $\xi_0$ of $X^\circ$ over a field $\Omega \supseteq F$ whose closure is $U$, with `IsCptGen`, and a model $M$ of the Lie algebra at $\xi_0$ with an $\mathcal{O}_E$-action $\rho$. Suppose:

1. `Z.IsGeom`: each element of $\Omega$ algebraic over $F$ lies in $F$;
2. `FlatOnModel Z τ φ`: `IsLineFn U τ φ`, and there are $a \in \bigwedge^p V$, $b \in \bigwedge^q V$ with `IsLineGenOn` for the $\tau$ and $\bar\tau$ eigenlattices on the generic fibre, such that $\varphi(y, v, w)$ is the value of $\alpha/\kappa'$ at $y$ whenever $a = \alpha\, b_1 \wedge \dots \wedge b_p$ and $b = \kappa'\, c_1 \wedge \dots \wedge c_q$ with $b_i, c_j$ of values $v_i, w_j$ at $y$ (`Represents`);
3. `IsLineFn U τ φ`.

**Theorem.** There is $t \in \mathbb{R}$ with `HasFinNorm U τ φ ℓ κ t`: $\log|\varphi(y, v, w)|_\kappa = t$ at each framed point $y$ over the fraction field of a discrete valuation ring where $v$ and $w$ are integral frames.

## Proof

1. **The ring $O$.** `mem_or_inv_mem` shows $x \in \beta(O)$ or $x^{-1} \in \beta(O)$ for each $x \in F$, and `exists_frac` makes $F$ the fraction field. `dvd_prime` shows that a uniformizer $\varpi$ divides $\ell$.
2. **The compactification.** `T.proper_normal_compactification` makes $Y$ proper with a normal compactification, and gives eigenspaces of dimensions $p$ and $q$ for $\tau$ and $\bar\tau$ in $V$. We take bases $v$, $w$ of them.
3. **A Hodge lattice.** `T.eigen_line_p_adic_bound` gives a Hodge lattice $\mathcal{H}$ with a degree condition at $\varpi$, from `SplitFibres` and `N3`. `T.hermitian_signature_basis` gives an adapted basis $u$.
4. **The sections.** From `FlatOnModel`, `exists_smul_iotaMulti` writes $a = \alpha \wedge v$ and $b = \kappa' \wedge w$ with $\kappa' \ne 0$.
5. **The order is constant.** `constClosed_of_isGeom` turns `IsGeom` into the closure condition `ConstClosed`. Then `T.hodge_lattice_valuation_agree` gives $M > 0$ and $k \in \mathbb{Z}$ that fix the order of $\alpha/\kappa'$ along the components.
6. **The value.** `T.eigen_line_p_adic_frame` turns this into the constant $t$.

## In the Lean code

The theorem is in [FiniteConstantAllHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FiniteConstantAllHolds.lean#L137). `FinConstFor` is in [FinConstFor.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/FinConstFor.lean#L17), and `FlatOnModel` and `CptOver` are in [IsFlatAnIffIsConstMul.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/IsFlatAnIffIsConstMul.lean#L164). Hypotheses 2 and 3 both contain `IsLineFn`. The proof drops the copy in `FlatOnModel` at [line 173](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FiniteConstantAllHolds.lean#L173) and uses the other one, although `FlatOnModel.isLineFn` gives it. We have not opened the proofs of the statement forms in steps 2, 3, 5 and 6. The Lean names the prime `p`, which is also the first part of the signature; here we call the prime $\ell$.
