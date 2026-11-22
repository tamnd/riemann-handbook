---
id: k5-top
title: The Hodge-Tate law for smoothed zeta classes
kind: theorem
decl: UpperTheory.V.Z.Kato.K5.top
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.KatoQuadraticCharacters.SmoothedZetaClasses.Imports
covers: 1882
status: drafted
drafted_by: writer@claude
---
This theorem gives a smoothed zeta class of a newform a Kummer presentation by polynomials in roots of unity, and computes the twisted sums of its logarithmic derivatives modulo powers of $\ell$. Under the name [`smoothedZetaClass_hodgeTateLaw`](/entry/smoothed-zeta-class-hodge-tate-law/) it goes into the proof of [the unramified zeta theorem](/entry/zeta-ur/). Its main input is [the coefficient law](/entry/hco/).

## Statement

Let $\ell$ be an odd prime, $\Omega = \overline{\mathbb{Q}}$, $\iota \colon \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, $e \geq 1$, and $A$ a valuation ring of $\Omega$. Let $W$ be a two-dimensional $\ell$-adic [[Galois representation|JQEYEQJY2G]] of $G_{\mathbb{Q}}$ that meets the conditions `Nf`, and $g$ a newform of weight $2e+1$ that meets `SrcUr`: $\ell$ does not divide the level of $g$, $a_\ell(g)$ is a unit, and $g$ is attached to a twist of $W$ with a condition on inertia. Let $X$ be a tower (the structure `Tower`, not unfolded here) whose $j$-function is holomorphic on the set `Hs`. Let $N \geq 5$ be prime to $\ell$, let $c, d$ and matrices in $\Gamma_1(N)$ be auxiliary data, and let $c_x \in \mathcal{O}$ for $x \in \mathbb{Z}/N$ be weights; each $x$ with $c_x \neq 0$ satisfies the conditions `AdmissibleNewformZetaData`. Let $j \colon \Omega \to \overline{\mathbb{Q}}_\ell$ be an embedding with $A = \{y : |j(y)| \leq 1\}$.

Let $Y_r \colon G_{\mathbb{Q}} \times (\mathbb{Z}/\ell^r)^\times \to \overline{\mathbb{Q}}_\ell^2$ be a family of zeta classes. Each $Y_r$ is a sum $\sum_x c_x Y_{x,r}$ of zeta systems, satisfies $Y_r(st, y) = Y_r(s, y) + \rho(s)\, Y_r(t, y\,\kappa(s))$, with $\rho$ a twist of $W$ (the map `rhoK`) and $\kappa$ the inverse cyclotomic character mod $\ell^r$, is continuous, and has integral second coordinate. Let $\chi$ be a [[Dirichlet character|JR4QSEFXWF]] mod $N$ with values in $\mathbb{Z}_\ell$, and $\lambda$ a linear form on sequences with finite support that satisfies the congruence conditions `IsLamFR2`. Let $d_0 \geq 2$ be prime to $\ell$. Put
$$Z_r(s, y) = Y_r(s, y)_1 - d_0\, Y_r(s, y d_0)_1.$$

**Theorem.** There are $m_0, c_1$, a constant $\kappa \neq 0$ and units $v(m)$ with $v(m+1) \equiv v(m) \bmod \ell^m$, and a compatible system of primitive $\ell^m$-th roots of unity $\zeta_m$, such that for each $m \geq m_0$ there are polynomials $P_i$ over $A$ and $o_i \in \mathcal{O}$ that give a Kummer presentation of $Z$ on inertia, and for each primitive character $\psi$ mod $\ell^m$:
$$\begin{aligned} &\sum_b \psi(b) \sum_i o_i\, j\Bigl(\frac{\zeta_m^b P_i'(\zeta_m^b)}{P_i(\zeta_m^b)}\Bigr) \\ &\quad \equiv \bigl(1 - d_0 \psi^{-1}(d_0)\bigr)\, v(m)\, \kappa\, \Bigl(\sum_a \psi(a)\, j(\zeta_m)^a\Bigr)\, \psi^{-1}(N)\, \lambda(E_{m,\psi}) \pmod{\ell^{m - c_1}}.\end{aligned}$$
Here $E_{m,\psi}$ is the sequence $\sum_x c_x \cdot \mathrm{chiProj}(\dots, \psi, \chi, c, d, x)$: an average over $(\mathbb{Z}/N)^\times$ weighted by $\chi$ of the terms `coPtSb`, which we have not unfolded.

The names point to the Euler system of K. Kato (Astérisque 295, 2004). We do not claim that this exact statement is in that paper.

## Proof

The proof is `law_of_inputs` applied to two theorems. [`K5.hco`](/entry/hco/) gives, for each $x$, a congruence for $Y_{x}$ modulo coboundaries. `exists_pres_smoothed` gives the polynomial presentation of the smoothed class. Then `law_of_inputs` does this:

1. If some $c_x \neq 0$, it uses `rho_on_dec` to get the shape of $\rho$ on inertia that `hco` asks for, and applies `hco`. If all $c_x = 0$, the claim is trivial.
2. `htCoL_smooth` subtracts the laws at $y$ and $y d_0$ (a lift of $d_0$ that is $1$ mod $N$ comes from the Chinese remainder theorem). `sum_chiVal` and `sum_translate` compute the twisted character sums. These give the factor $1 - d_0\psi^{-1}(d_0)$.
3. `localGlue` and `law_of_parts` give the form `HTLawCsOfCoef`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [Imports.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SmoothedZetaClasses/Imports.lean#L11). The lemmas:

- `law_of_inputs` in [SumTranslate.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/SumTranslate.lean#L121).
- `exists_pres_smoothed` in [SmoothedPresOfShCoc.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/SmoothedPresOfShCoc.lean#L197). It takes $m_0 = c_0' = 0$.
- `law_of_parts` in [NormLPowLe.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/NormLPowLe.lean#L110).

The constant $\alpha$ enters only through `AdmissibleHodgeTateZetaClassParams`: $|\alpha| = 1$, and $U_\ell$ multiplies the projection by $\alpha$. The file name `Imports.lean` hides a theorem.
