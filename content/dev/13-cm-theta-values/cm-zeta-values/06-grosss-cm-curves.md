---
title: Gross's CM curves
decls:
  - GlobalTheory.Published.cmCurveGoodOutsidePrime
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gross's CM curves

This section proves the existence of Gross's curves. Let $p > 3$ be a prime with $p \equiv 3 \pmod 4$. The curve has complex multiplication by the ring of integers of $\mathbb{Q}(\sqrt{-p})$, it is defined over $F = \mathbb{Q}(j)$, it has good reduction at each prime of $F$ not over $p$, and its minimal discriminant is $-p^3$ at every prime. The statement is the literature entry [Gross's curves](/entry/cm-curve-good-outside-prime-st-of-literature/), and the code proves it. It is a field of the bundle of published results in [the record of published inputs](/step/published-results-eigen/), and the code applies it with $p = d$, where $-d$ is the discriminant of the host field. The background is in [Gross's curves](/learn/elliptic-curves/#grosss-curves), [reduction and minimal models](/learn/elliptic-curves/#reduction-and-minimal-models) and [quadratic twists](/learn/elliptic-curves/#quadratic-twists).

Write $\sqrt{-p} = i\sqrt p \in \mathbb{C}$ and $K = \mathbb{Q}(\sqrt{-p}) \subset \mathbb{C}$. For a lattice $L \subset \mathbb{C}$ let $E_L$ be the curve $y^2 = x^3 - \tfrac14 g_2(L)\, x - \tfrac14 g_3(L)$ over $\mathbb{C}$. Its points are $(\wp, \wp'/2)$, and $j(L)$ is its $j$-invariant.

**Definition 1.6.1 (integer lattice).** A lattice $L \subset \mathbb{C}$ is *the integer lattice of $K$* if, for each $z \in \mathbb{C}$, $z \in L$ exactly when $z \in K$ and $z$ is an algebraic integer.

So $L = \mathcal{O}_K$ as a subset of $\mathbb{C}$. Since $p \equiv 3 \pmod 4$, $\mathcal{O}_K = \mathbb{Z}[(1 + \sqrt{-p})/2]$, and $\sqrt{-p}\, L \subset L$.

**Definition 1.6.2 (good reduction outside $p$).** Let $F$ be a number field and $A$ a Weierstrass curve over $F$. Then $A$ has *good reduction outside $p$* if, for each prime $v$ of $\mathcal{O}_F$ with $p \notin v$, there is a change of variables $C$ over $F$ such that $C \cdot A$ is a minimal model at $v$ with good reduction.

**Definition 1.6.3 (minimal discriminant).** Let $D \in F$. The curve $A$ has *minimal discriminant $D$* if, for each prime $v$ of $\mathcal{O}_F$, there are a change of variables $C$ over $F$ and a unit $u$ of the local ring $\mathcal{O}_{F,v}$ such that $C \cdot A$ is a minimal model at $v$ and $\Delta(C \cdot A) = u D$.

**Definition 1.6.4 (good CM curve).** Let $F \subset \mathbb{C}$ be a subfield and $A$ a Weierstrass curve over $F$. Then $A$ is a *good CM curve for $p$* if $F$ is a number field, $A$ is elliptic, and there is an integer lattice $L$ of $K$ with
$$F = \mathbb{Q}(j(L)), \qquad j(A) = j(L),$$
such that $A$ has good reduction outside $p$.

Any two integer lattices of $K$ are equal as sets, so $j(L)$ does not depend on the choice of $L$.

**Theorem 1.6.5 (Gross's curves).** Let $p$ be a prime with $p \equiv 3 \pmod 4$ and $p > 3$. Then there are a subfield $F \subset \mathbb{C}$ that is a number field and a Weierstrass curve $A$ over $F$ such that $A$ is a good CM curve for $p$ and $A$ has minimal discriminant $-p^3$.

Lean: `GlobalTheory.Published.cmCurveGoodOutsidePrime`.

The proof uses five lemmas about CM curves. We state them in the form that the proof applies.

**Lemma 1.6.6 (lattice data).** Let $L_0$ be the integer lattice of $K$. Then $g_2(L_0) \neq 0$, $g_3(L_0) \neq 0$ and $\sqrt{-p}\, L_0 \subset L_0$. If $\beta \in \mathbb{C}$ is not real and $\beta L \subset L$ for a lattice $L$, then $j(L)$ is an algebraic integer.

**Lemma 1.6.7 (kernel datum).** Let $F = \mathbb{Q}(j(L_0))$. There are a lattice $L$ and a point $t \in \mathbb{C}$ with $j(L) = j(L_0)$ such that:

1. $\sqrt{-p}\, L \subset L$;
2. $g_2(L)$ and $g_3(L)$ lie in $F$;
3. $t \notin L$ and $\sqrt{-p}\, t \in L$;
4. the product $\prod_k \wp'(kt; L)$ lies in $F$, where $k$ runs over the integers $0 < k < p$ that are nonzero squares modulo $p$.

So $t$ is a nonzero point of the kernel of $\sqrt{-p}$ on $E_L$. The code gets the first three parts with some lattice, and then it rescales the lattice to get the fourth part.

**Lemma 1.6.8 (local model of the twist).** Let $L$ and $t$ be as in the kernel datum, let $d = 1$ if $p \equiv 3 \pmod 8$ and $d = -p$ if $p \equiv 7 \pmod 8$, and let $A_d$ be the curve
$$y^2 = x^3 - \tfrac14 d^2 g_2(L)\, x - \tfrac14 d^3 g_3(L).$$
For each valuation subring $V$ of $\mathbb{C}$, there is a change of variables with coefficients in $F$ that takes $A_d$ to a model with coefficients in $V$ and with $v_V(\Delta) = v_V(-p^3)$.

**Lemma 1.6.9 (minimality).** Let $w$ be a prime of a number field $F$ with $p \notin w^3$. If a model $W$ of a curve over $F$ is integral at $w$ and $\Delta(W) = u \cdot (-p^3)$ with $u$ a unit at $w$, then $W$ is minimal at $w$.

**Lemma 1.6.10 (ramification).** For each prime $w$ of $\mathbb{Q}(j(L_0))$, $p \notin w^3$.

*Proof of the theorem.* Let $L_0$ be the integer lattice of $K$. It exists since $\mathcal{O}_K$ is a lattice in $\mathbb{C}$.

*The field.* By the lattice data lemma, $\sqrt{-p}\, L_0 \subset L_0$. The number $\sqrt{-p}$ is not real, so $j(L_0)$ is an algebraic integer. Then $F = \mathbb{Q}(j(L_0))$ is a finite extension of $\mathbb{Q}$, so it is a number field.

*The lattice.* The kernel datum lemma gives $L$ and $t$ with $j(L) = j(L_0)$, with $g_2(L), g_3(L) \in F$, and with the product of $\wp'(kt; L)$ in $F$.

*The curve.* Let $d$ be as in the local model lemma. The numbers $a = -g_2(L)/4$ and $b = -g_3(L)/4$ lie in $F$. Let $A$ be the curve over $F$
$$y^2 = x^3 + d^2 a\, x + d^3 b.$$
Over $\mathbb{C}$, $A$ is $A_d$. A direct computation gives
$$\begin{aligned}
\Delta(A) &= d^6\, \Delta(E_L), \\
c_4(A) &= d^2\, c_4(E_L).
\end{aligned}$$
Since $d \neq 0$ and $\Delta(E_L) \neq 0$, $\Delta(A) \neq 0$ and $A$ is elliptic. Since $j = c_4^3/\Delta$, the factors $d^6$ cancel, and $j(A) = j(E_L) = j(L) = j(L_0)$.

*Minimal discriminant.* Let $w$ be a prime of $\mathcal{O}_F$. There is a valuation subring $V$ of $\mathbb{C}$ whose trace on $F$ is the local ring of $F$ at $w$. The local model lemma gives a model of $A$ over $F$ that is integral for $V$ and has $v_V(\Delta) = v_V(-p^3)$. Then there are a change of variables $C$ over $F$ and a unit $u$ at $w$ such that $C \cdot A$ is integral at $w$ and $\Delta(C \cdot A) = u \cdot (-p^3)$. By the ramification lemma, $p \notin w^3$. The minimality lemma then shows that $C \cdot A$ is minimal at $w$.

The idea of the minimality lemma is as follows. Since $p \notin w^3$, $v_w(p) \le 2$, so $v_w(\Delta(C \cdot A)) \le 6 < 12$. A change of variables multiplies $\Delta$ by $u^{-12}$. Thus no integral model has a smaller value of $v_w(\Delta)$.

*Good reduction outside $p$.* Let $v$ be a prime with $p \notin v$. Then $p$ is a unit at $v$, so $u \cdot (-p^3)$ is a unit at $v$. The minimal model at $v$ has a unit discriminant, so it has good reduction.

*Assembly.* The field $F$ is a number field, $A$ is elliptic, $L_0$ is the integer lattice of $K$, $F = \mathbb{Q}(j(L_0))$, $j(A) = j(L_0)$, and $A$ has good reduction outside $p$. So $A$ is a good CM curve for $p$, and its minimal discriminant is $-p^3$. $\square$

The choice of $d$ is the only step that uses the class of $p$ modulo $8$. The twist by $-p$ multiplies $\Delta$ by $p^6$, and it does not change $j$. The local model lemma holds for every valuation subring $V$ of $\mathbb{C}$, so it covers the primes over $2$ and over $p$ as well as the other primes.

**Remark 1.6.11 (Formalization).** The theorem is in the namespace `Published`, but the code proves it ([CmCurveGoodOutsidePrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CmCurveGoodOutsidePrime.lean#L47)). The curve $E_L$ is `latticeCurve`, with coefficients $(0, 0, 0, -g_2/4, -g_3/4)$. The twist is `shortTwist`, and the kernel datum is the structure `Datum`. The statement `ModelAt` asks for a change of variables with $u, r, s, t \in F$ and a model with coefficients in $V$. The proof does not unfold the five lemmas: `integersLattice_g2_g3_ne_zero_and_mulStable`, `isIntegral_j_of_nonreal_multiplier`, `exists_sqrtNegPrimeKernelDatum_of_integersLattice` with `exists_rescaled_lattice_prodDerivWeierstrassP_mem`, `quadraticTwist_cmCurve_model_discriminant_negPrimeCube`, `isMinimal_of_discr_eq_unit_mul_neg_prime_cube` and `natCast_notMem_cube_prime_adjoin_jInvariant_sqrtNeg`. It also uses `exists_valuationSubring_complex_restrict_eq_at_prime` and `exists_variableChange_isIntegral_of_modelAt` to pass from $V$ to the local ring at $w$. The identities for $\Delta$, $c_4$ and $j$ of the twist are proved in the file by `ring` and `field_simp`.
