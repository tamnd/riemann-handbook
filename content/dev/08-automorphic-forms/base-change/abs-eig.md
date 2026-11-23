---
id: abs-eig
title: An Iwahori eigenvector with ordered Satake parameters for a quasi-split unitary group
kind: theorem
decl: PositivityTheory.Rg.BcB.F.Eig.absEig
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.SatakeExponents.UniformizerValuations.InertEigenvalues.AbsEigB
covers: 734
status: drafted
drafted_by: writer@claude
---
Let $\rho$ be an irreducible unramified representation of a quasi-split unitary group over a local field. This theorem gives a nonzero Iwahori fixed vector that is an eigenvector of the Hecke operators of strictly dominant diagonal elements. The eigenvalues come from a reordering $\beta$ of the Satake parameters. It is the first input of [Iwahori eigenvalues at an inert place](/entry/eig-inert/). See also [unramified representations](/learn/representations/#unramified-representations).

## Statement

Let $L$ be a complete field with a discrete valuation, $\bar x = \sigma(x)$ an involution of $L$ that keeps the valuation, and $\varpi$ a uniformizer with $\bar\varpi = \varpi$. Suppose that the residue field has $q^2$ elements and that $\sigma$ acts on it nontrivially (`IsUnramInv`). Let $G = \{g \in \mathrm{GL}_n(L) : \bar g^{\mathsf T} J g = J\}$ with $J$ the antidiagonal matrix of ones, $K = G \cap \mathrm{GL}_n(\mathcal{O}_L)$, $I$ the Iwahori subgroup of $G$ (`IwU`), and $m = \lfloor n/2 \rfloor$. For $g \in G$, call an operator $T$ on $V^I$ a *Hecke operator* of $g$ if $\ell(\rho(g)v) = \ell(Tv)$ for each $I$-invariant linear form $\ell$ (`IsHeckeOpG`). For a diagonal $t \in G$ with valuations $a_i = \operatorname{ord}(t_{ii})$ put
$$\chi_\beta(t) = \prod_{i=1}^{m} \beta_i^{a_i}\, q^{-(n+1-2i)a_i}.$$

**Theorem.** Let $\rho$ be an irreducible admissible representation of $G$ on $V$, spherical for $K$ with Satake parameters $\alpha \in (\mathbb{C}^\times)^m$ (`HasSatU`). Then there is $\beta \in (\mathbb{C}^\times)^m$ such that:

1. $\beta$ comes from $\alpha$ by a permutation and by inverting some entries (`WeylConjU`);
2. $|\beta_1| \ge \dots \ge |\beta_m| \ge 1$;
3. there is a nonzero $y \in V^I$ with $T y = \chi_\beta(t)\, y$ for each diagonal $t \in G$ with $a_1 > a_2 > \dots > a_n$ and each Hecke operator $T$ of $t$.

## Proof

1. **An embedding.** [`extremeU`](/entry/extreme-u/) gives $\beta$ with 1 and 2, and an injective $G$-map $f$ from $V$ to the principal series $I(\beta)$ of functions $\varphi$ on $G$ with $\varphi(bg) = \chi_\beta(b)\varphi(g)$ for upper triangular $b \in G$.
2. **Iwahori factorization.** `iwahori_u` gives a datum `CassData` for $G$: the groups $I$, upper and lower unipotent $N$ and $N^-$, the diagonal torus, and $I = (I \cap N^-)(I \cap T)(I \cap N)$ in both orders.
3. **An eigenform.** Let $\mu(x) = f(x)(1)$ on $V^I$. For dominant $t$ and a Hecke operator $T$ of $t$, $\mu(T x) = \chi_\beta(t)\mu(x)$ (`hecke_fun`). Indeed $\mu$ vanishes on the kernel of the Jacquet module for $N$, and $T x$ and $\rho(t)x$ have the same image in it (`jacquet_hecke`).
4. **$\mu \neq 0$** (`exists_ne_zero_at_one`). A nonzero $K$-fixed vector $x$ lies in $V^I$. If $f(x)(1) = 0$, then $f(x) = 0$ by the uniqueness of the spherical function in $I(\beta)$ (`SphericalExistsU`), and $f$ is injective.
5. **A common eigenvector.** $V^I$ has finite dimension, and Hecke operators of dominant elements commute (`dominant_hecke_operators_commute`). A commuting family with a nonzero common eigenform $\mu$ has a common eigenvector with the same eigenvalues (`iInf_maxGenEig_ne_bot`, `exists_common_eigvec`).
6. `dom_u`: a strictly dominant diagonal $t$ is dominant for the datum.

## In the Lean code

The theorem is in [AbsEigB.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/InertEigenvalues/AbsEigB.lean#L269), with steps 3 to 5 in `main_D` at line 224 of the same file. The statement `AbsEig` is in [EigInert.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/EigInert.lean#L25), and $\chi_\beta$ is `chiDeltaU` in [StatementF.lean](lean:Formalism/SatakeDualWeyl/StatementF.lean#L40). `jacquet_hecke`, `iwahori_u` and `dom_u` are second names for `GlobalTheory.T` statements, in [JacquetLemma.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/StrictDominance/JointGeneralisedEigenvectors/JacquetLemma.lean#L19); we have not unfolded their proofs.

The irreducibility of $\rho$ is used only by `extremeU`. The Lean indices run from 0, so the exponent of $q$ appears as $-(n-1-2i)a_i$.
