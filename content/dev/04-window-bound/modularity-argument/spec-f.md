---
id: spec-f
title: An eigenform on the norm one quaternion group has a partner on U(3) or on the quaternion units
kind: theorem
decl: UpperTheory.V.Z.Sym.So.specF
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.SymmetricPowerTransfer.GeneralizedEigenspaces.CharacterShapes.UnifLtOne
covers: 1782
status: drafted
drafted_by: writer@claude
---
This theorem is the dichotomy over a totally real field $F$. An eigenform on the norm one group $D^1$ of a quaternion algebra gives an eigenform on a definite $U(3)$ with the same parameters, or one on $D^\times$ with the squared parameters. The proof compares traces through [the trace identity](/entry/t-fid0/) and separates characters. [The core step](/entry/core/) uses it after it moves a form from $U(2)$ over a CM field to $D^1$.

## Statement

Let $F$ be a totally real field, $\Delta \in F$ totally negative, and $E = F(\sqrt{\Delta})$. Let $U_3$ be the unitary group of the identity hermitian form in three variables for $E/F$, with the conjugation $\theta$. Let $D^\times$ be the group of matrices $\begin{pmatrix} \alpha & \beta \\ -\bar\beta & \bar\alpha \end{pmatrix}$ with $\alpha, \beta \in E$, and $D^1$ its subgroup of determinant 1. Let $A$ be data with `A.Ok`: a nonempty finite set $\Sigma$ of places where $\Delta$ is a square, local levels there, and a character $\chi$.

A space of forms on $G$ is the set of $\varphi \colon G(\mathbb{A}_f) \to V$ with $\varphi(\gamma g) = W(\gamma)\varphi(g)$ for rational $\gamma$ and $\varphi(gu) = \omega(u)\varphi(g)$ for $u$ in a level. The conditions `IsBG`, `IsBS` (at a finite adele $x$ of $D^\times$) and `IsBK` fix the levels and tie the three weights to one function $c$ on $F$: the trace of $W$ at an element with invariant $\tau$ is $c(\tau)$.

Let $a = (a_v)_{v \in \Sigma}$ be characters of $F_v^\times$. The cone is the set of $t = (t_v)$ with $|t_v| < |\varpi_v|^2$. `EigS` for $a$ on $D^1$ says that for $t$ in the cone the double coset of $\mathrm{diag}(t, t^{-1})$ acts by $\mathrm{ex}_S(a, t) = \prod_{v \in \Sigma} \delta^{-1/2}(t_v, t_v^{-1})\, a_v(t_v)$. `EigG` for $a$ on $U_3$ is the same for all dominant diagonal $d$, with the character $(a_v, 1, a_v^{-1})$. `EigK` on $D^\times$ is the same as `EigS`, at the level of $D^\times$.

**Theorem.** Let $x$ be a finite adele of $D^\times$ with $x_v = 1$ for $v \in \Sigma$. Let $B_G$, $B_S$, $B_K$ be spaces of forms, with finite dimensional weights, that satisfy `IsBG`, `IsBS` at $x$ and `IsBK` for the same $c$. Let $\varphi \ne 0$ in $B_S$ satisfy `EigS` for $a$. Then $B_G$ has a nonzero form with `EigG` for $a$, or $B_K$ has a nonzero form with `EigK` for $a^2$.

## Proof

1. **The trace identity.** [`tFId0`](/entry/t-fid0/) at $x$ gives $x_0 = x, x_1, \dots, x_n$ and reals $c_1 > 0$, $c_2$ such that for $t$ in the cone
$$\operatorname{tr}(R_\theta(f_G^t)) = c_1 \sum_{i=0}^n \operatorname{tr}(R(f_S^{t, x_i})) + c_2 \operatorname{tr}(R(f_K^t)).$$
The private lemma `bases` gives a space of forms at each $x_i$. `finG`, `finS` and `finK` make all spaces finite dimensional.
2. **The $U_3$ side.** `gOpsEx` and `gSpec` write the left side as $\sum_i b_i \beta_i(t)$, with $\beta_i$ multiplicative on the cone. If $b_i \ne 0$ and $\beta_i = \mathrm{ex}_S(a, \cdot)$, there is a nonzero form with `EigG` for $a$.
3. **The other sides.** `sOps` and `kSpec` show that $t \mapsto R(f^t)$ is multiplicative on the cone. On $D^1$ it is the double coset operator, so $\varphi$ is an eigenvector with character $\mathrm{ex}_S(a, \cdot)$. On $D^\times$, by `kSpec`, an eigenvector with this character satisfies `EigK` for $a^2$.
4. **Separation.** `posSpec` says: suppose that $\sum_i b_i \beta_i = c_1 \sum_j \operatorname{tr} u_j + c_2 \operatorname{tr} w$ on a commutative semigroup, with $c_1 > 0$. Suppose that a character $\chi \ne 0$ is an eigencharacter of some $u_j$. Then $\chi = \beta_i$ with $b_i \ne 0$, or $\chi$ is an eigencharacter of $w$. Its proof is linear independence of characters. Apply it with $\chi = \mathrm{ex}_S(a, \cdot)$, which is not zero by `exS_ne`.

## In the Lean code

The theorem is in [UnifLtOne.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GeneralizedEigenspaces/CharacterShapes/UnifLtOne.lean#L73). `SpecF` is in [GlobIn.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GeneralizedEigenspaces/CharacterShapes/GlobIn.lean#L120). The statements of the lemmas are in [UnitaryThreeTestFunctionHeckeRelations.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GeneralizedEigenspaces/CharacterShapes/UnitaryThreeTestFunctionHeckeRelations.lean#L121).

- The structure `GlobIn` in GlobIn.lean has a field of type `TFId0`, but `specF` calls `tFId0` directly.
- The constant $c_2$ has no sign condition. Only $c_1 > 0$ is used.
- The operator $R(f)$ is `Base.Tw.R`, defined as 0 when $f$ gives no operator on the forms.
