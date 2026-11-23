---
title: Theta points at one level
decls:
  - GlobalTheory.T.exists_object_with_thetaPoint_of_degenerationSeries
  - GlobalTheory.Ex.OneLevel.exists_full_theta
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta points at one level

Let $S$ be a series datum for an arc $a$ in a field $K$, as in [the first section](/entry/exists-arc-series-integral-algebraic-over-power-series/). In this section we prove that, for each odd prime $n$ that is a unit in $O'$ and prime to $d$, and each $j \geq 2$, the values $v_{n^j}$ of $S$ form the theta point of level $n^j$ of an object with full level over $K$. The proof checks the two conditions of a criterion for theta points: the values satisfy every complex theta relation, which follows from the identity principle of [the second section](/entry/theta-series-identity-principle-complex-points/), and each coset of $n^{j-1}\Lambda$ carries a nonzero value, which follows from the integrality of $S$. The result is used in [the next section](/entry/exists-point/) to build a moduli point over the power series ring.

### A criterion for theta points

We use the notation of the first two sections. In particular, an object with full level is a polarized abelian variety with an action of $\mathcal{O}_E$ and a Tate isomorphism, and a complex theta relation of level $m$ is a homogeneous polynomial over $\mathbb{Z}[x, y]$ that vanishes on all complex theta points of level $m$.

The criterion below is a converse to the classical fact that theta null points satisfy the theta relations. It is proved in the Lean development outside this chapter, and we use it as an input.

**Theorem 6.3.1 (Criterion for theta points).** Assume the seven inputs and let $Y$ be a model of $X_o$. Let $K$ be an algebraically closed field of characteristic $0$, let $n$ be an odd prime, let $j \geq 2$, let $\rho, z \in K$ and let $v : \Lambda \to K$. Assume that:

1. the pair $(z, \rho)$ is compatible at level $n^{2j}$;
2. $G(v) = 0$ for every complex theta relation $G$ of level $n^j$, with the coefficients mapped to $K$ by $x \mapsto z$ and $y \mapsto \rho$;
3. for every $x \in \Lambda$ there is $h \in \Lambda$ with $v(x + n^{j-1} h) \neq 0$.

Then there is an object $o$ with full level over $K$ with $\rho(o) = \rho$, $\zeta_{n^{2j}}(o) = z$ and theta point of level $n^j$ equal to $v$.

Lean: `GlobalTheory.T.mem_thetaPoints_of_closure_coset_condition`.

The first condition is automatic in our setting, by the following arithmetic lemma.

**Lemma 6.3.2 (Compatibility).** Let $N \geq 1$ with $d \nmid N$. Let $K$ be a field, let $\zeta \in K$ be a primitive $N$-th root of unity and let $\rho \in K$ with $\rho^2 = -d$. Then $(\zeta, \rho)$ is compatible at level $N$.

Lean: `GlobalTheory.Ex.OneLevel.compat_of_not_dvd`.

*Proof.* Write $z = \zeta_N^{\mathbb{C}}$ and let $\mathbb{Z}[z]$ be the ring it generates. Each $c \in \mathbb{Z}[x, y]$ has polynomials $a, b \in \mathbb{Z}[x]$ with $c(\zeta', \rho') = a(\zeta') + \rho' b(\zeta')$ whenever $\rho'^2 = -d$, in every ring. Assume $a(z) + \rho_{\mathbb{C}} b(z) = 0$. Then $A = a(z)$ and $B = b(z)$ satisfy $A^2 = -d B^2$ in $\mathbb{Z}[z]$.

We claim that $B = 0$. Since $d$ is prime and prime to $N$, some power $d^k$ with $k \geq 1$ has $z^{d^k} = z$, and then $d$ divides $y^{d^k} - y$ for every $y \in \mathbb{Z}[z]$, by the binomial theorem. So if $d \mid y^2$ then $d \mid y$. From $A^2 = -d B^2$ we get $d \mid A$, say $A = d A'$, then $B^2 = -d A'^2$ and $d \mid B$, say $B = d B'$, and $A'^2 = -d B'^2$. If $B \neq 0$, then $B'$ is a proper divisor of $B$ with the same property. The ring $\mathbb{Z}[z]$ is noetherian, since $z$ is integral, so there is no infinite chain of proper divisors, and $B = 0$.

So $b(z) = 0$ and then $a(z) = 0$. The minimal polynomial of $z$ over $\mathbb{Z}$ is the cyclotomic polynomial $\Phi_N$, so $\Phi_N$ divides $a$ and $b$ in $\mathbb{Z}[x]$. Since $\zeta$ is a primitive $N$-th root of unity, $\Phi_N(\zeta) = 0$, so $a(\zeta) = b(\zeta) = 0$ and $c(\zeta, \rho) = 0$. $\square$

### The theorem

**Theorem 6.3.3 (Theta points of a series datum).** Assume the seven inputs. Let $Y$ be a model of $X_o$, let $(O', \varpi)$ be an arc base, let $a$ be an arc over $(O', b)$ and let $K$ be as in the theorem on series of theta values. Let $S$ be a series datum for $a$ in $K$, with lift $A$. Let $n$ be an odd prime that is a unit in $O'$, with $n \nmid d$, and let $j \geq 2$. Then there is an object $o$ with full level over $K$ with
$$\rho(o) = \rho(A), \qquad \zeta_{n^{2j}}(o) = \zeta_{n^{2j}}(A),$$
and with theta point of level $n^j$ equal to $v_{n^j}$.

Lean: `GlobalTheory.T.exists_object_with_thetaPoint_of_degenerationSeries` (also `GlobalTheory.Ex.OneLevel.exists_full_theta`, a second name).

*Proof.* Put $m = n^j$, which is odd. We check the three conditions of the criterion for theta points, with $\rho = \rho(A)$, $z = \zeta_{m^2}(A)$ and $v = v_m$.

*Condition 1.* Since $d$ and $n$ are primes and $n \nmid d$, also $d \nmid m^2$. The root $\zeta_{m^2}(A)$ is primitive and $\rho(A)^2 = -d$, so the lemma on compatibility applies.

*Condition 3.* Take the trivial valuation ring $S = K$. It contains the image of $O'[[X]]$, and $X$ is a unit in it, since $X = r(1)$ is the first of a system of roots and so is nonzero. By the first property of a series datum, for each $x$ there is $h$ with $v_m(x + n^{j-1} h)$ a unit of $K$, so nonzero.

*Condition 2.* Let $G$ be a complex theta relation of level $m$, of degree $e$, and assume that $G(v_m) \neq 0$. Choose a test point $(C, \gamma)$ of $i : O'[[X]] \to K$, which exists, and put $u = \gamma(i(X))$, so $|u| < 1$. The second property of a series datum gives an integral lift $A'$ of $a$ to $C$ over $A$, with $\rho(A') = \gamma(\rho(A))$, $\zeta(A') = \gamma(\zeta(A))$ and roots $r' = \gamma \circ r$. Put $t = r'(m^2)$. Then $t^{m^2} = u$, by the root relations, so $|t| < 1$.

The twist of $N(A')$ by $(\beta', u)$ is the twist by $(m^2 \beta', t)$. Choose for each $x$ the unique class $p(x)$ that is twist-related to $q'_{m^2}(x)$ by $t$. The series datum gives $s \in C^\times$ with
$$\gamma(v_m(x)) = s \cdot \vartheta_m(p(x)) \quad \text{for all } x.$$
The form $m^2 \beta'$ is balanced, because $\beta'$ is the form of the arc under the comparison, and the form of an arc is balanced. By the identity principle for theta relations, applied over $C$ to the lift $A'$, the form $m^2\beta'$ and the level $m$, the formal theta series of $A'$ satisfy $G$. The lemma on compatibility gives the hypothesis of that theorem.

Since $A'$ is integral and $|t| < 1$, the formal theta series converge at $t$, and their values are the twisted theta values $\vartheta_m(p(x))$, up to the common factor of the previous section. So $G$ vanishes at $x \mapsto \vartheta_m(p(x))$. Since $G$ is homogeneous of degree $e$,
$$\gamma\bigl(G(v_m)\bigr) = s^e\, G\bigl(x \mapsto \vartheta_m(p(x))\bigr) = 0.$$
Here we used that $\gamma$ maps the constants $\zeta_{m^2}(A)$ and $\rho(A)$ to those of $A'$. Since $\gamma$ is a field map, it is injective, so $G(v_m) = 0$, a contradiction.

The criterion now gives the object $o$. $\square$

**Remark 6.3.4 (Formalization).** The Lean proof is in [ExistsObjectWithThetaPointOfDegenerationSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsObjectWithThetaPointOfDegenerationSeries.lean#L158), and the criterion for theta points is stated in [MemThetaPointsOfClosureCosetConditionStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/MemThetaPointsOfClosureCosetConditionStatement.lean#L11). The theorem covers only $j \geq 2$, as the criterion does; the level $n^1$ is not needed later. The existence of a test point is `Ser.base.not_allC_false`, used in a proof by contradiction. The convergence of the formal theta series at $t$ is `eval_twist_tx_eq_zero_of_aeval_arcTx`, with the norm bounds of an integral lift (`UnitNorm.norms_of_arc_input`); we did not unfold these. The rescaling of the form is `tx_scale`.
