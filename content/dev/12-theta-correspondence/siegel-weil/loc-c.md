---
id: loc-c
title: The local Whittaker integral at a good unramified place
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Gunr.locC
module: Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.UnramifiedWhittaker.CFinal
covers: 387
status: drafted
drafted_by: writer@claude
---
This theorem computes the local Whittaker integral of the Siegel-Weil formula at a finite place where everything is unramified. The answer is a finite product of local zeta factors. It is a local input to the Siegel-Weil formula that the step [every character](/step/every-character/) uses. Its two users are `unrWhitX` and `unrWhit`, which add the fact that almost all places are good.

## Statement

Let $F \subseteq E$ be number fields and $\sigma$ an automorphism of $E$ over $F$. Let $J \in M_M(E)$ and $T \in M_n(E)$ with $T$ Hermitian. Let $v$ be a finite place of $F$ with residue field of size $q$, and let $\psi_v$ be an additive character of $F_v$. Let $S$ be the integral elements of $F_v \otimes E$ in a fixed basis, with uniformiser $\varpi$ of $F_v$. We call $v$ good if:

- $S$ is complete and separated, $S/\varpi$ has $q^2$ elements, and $\varepsilon = -1$ exactly when $S/\varpi$ is a field (the inert case), else $\varepsilon = 1$;
- $\lVert 2 \rVert_v = 1$ and $S$ is its own trace dual;
- $J$ and $T$ have entries in $S$ and are unimodular;
- $\psi_v$ is continuous with conductor $\mathcal{O}_v$.

For $z \in \mathbb{C}$ and a Hermitian $b$ over $F_v$, put

$$W(b, z) = \nu(b)^{-(z - (M-n)/2)}\, \psi_v(-\langle T, b \rangle) \int \mathbf{1}_{L}(Y)\, \psi_v(\langle b, Y^* J Y \rangle)\, d\mu_v(Y),$$

where $L$ is the standard lattice, $\langle S, T \rangle = \tfrac12 \operatorname{Tr}(\operatorname{tr}(ST))$, and $\nu(b) = \lambda(L + bL)/\lambda(L)$.

**Theorem.** Let $v$ be good, and let $\mu_v$ and $\nu_v$ be self-dual Haar measures. If $n^2 < \operatorname{Re} z$, then $W(\cdot, z)$ is $\nu_v$-integrable and

$$\int W(b, z)\, d\nu_v(b) = \prod_{i=0}^{n-1} \bigl(1 - \varepsilon^{M+i}\, q^{-(2z + n - i)}\bigr).$$

## Proof

The proof is `locC_of_steps`. `locC` feeds it fourteen lemmas.

1. **Periodicity.** $W(b + h) = W(b)$ for every integral Hermitian $h$. So $W$ factors through the quotient by the integral Hermitian lattice $H_0$, which has measure $1$.
2. **Classes.** Each class is $\varpi^{-k}B$ for some $k$ and some Hermitian $B$ modulo $\varpi^k$. These sets grow with $k$ and cover the quotient.
3. **Values.** Put $t = \varepsilon^M q^{-(2z+n)}$. On the class of $\varpi^{-k}B$ the value of $W$ is $t^{m} \psi_k(\operatorname{tr}(TB))$, where $q^{2m}$ is the size of the row space of $B$.
4. **Bound.** Since $n^2 < \operatorname{Re} z$, we have $q^{n^2}\lvert t \rvert < 1$. So every partial sum of $\lvert W \rvert$ is at most $1/(1 - q^{n^2}\lvert t \rvert)$.
5. **Polynomial identity.** For unimodular $T$ and $k \ge 1$, the sum over $B$ in step 3 is $\prod_{i<n}(1 - t(\varepsilon q)^i)$ (`unrPoly`).
6. **Limit.** The sum over classes is summable and equals the limit of the partial sums. The integral is that sum, since $\nu_v(H_0) = 1$. The product of step 5 is the right side.

## In the Lean code

The theorem is in [CFinal.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/UnramifiedWhittaker/CFinal.lean#L22). `LocC` and `GoodLoc` are in [TraceDual.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/UnramifiedWhittaker/TraceDual.lean#L42), and `locC_of_steps` is in [LocCMain.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/UnramifiedWhittaker/LocCMain.lean#L11). The fourteen inputs are second names in `GlobalTheory.T`, each proved by `first | exact …`. We have not opened their proofs. The condition $n^2 < \operatorname{Re} z$ is only used for the bound in step 4. It is stronger than the bound "for $\operatorname{Re} z > t$ for some $t$" that the users need.
