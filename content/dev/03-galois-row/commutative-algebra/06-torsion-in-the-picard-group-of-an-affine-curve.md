---
title: Torsion in the Picard group of an affine curve
decls:
  - UpperTheory.isFunctionField_and_charts_of_isCurve_of_isUnit
  - UpperTheory.curve_picard_of_selmerPicard_of_modelCurve
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Torsion in the Picard group of an affine curve

Let $B$ be a Dedekind domain of finite type over an algebraically closed field $k$, and let $q$ be invertible in $k$. This section proves that the $q$-torsion subgroup $\operatorname{Pic}(B)[q]$ is finite. The finiteness theorem for the étale cohomology of proper schemes, [Theorem 2.3](/entry/etale-topology-top/), uses it to show that $H^1(\operatorname{Spec} B, \mathbb{Z}/q(1))$ is finite: by the Kummer sequence of the previous section, this group is an extension of $\operatorname{Pic}(B)[q]$ by $B^\times / B^{\times q}$.

Classically, the result follows from the theory of the Jacobian: $\operatorname{Pic}(B)$ is a quotient of the Picard group of the smooth projective model of $B$, and the $q$-torsion of a Jacobian of genus $g$ is $(\mathbb{Z}/q)^{2g}$ (Mumford, *Abelian Varieties*, §4). The Lean proof avoids Jacobians. It works with the function field of $B$ and a Selmer group of functions whose divisors are divisible by $q$. It proves that this group is finite modulo $q$-th powers with the theorem of the previous section and a spreading-out argument.

### Function fields and Selmer groups

**Definition 5.6.1 (Function field).** Let $k$ be a field. A field $K \supseteq k$ is a *function field of one variable over $k$* if there is an element $u \in K$, transcendental over $k$, such that $K$ is a finite extension of $k(u)$. A *place* of $K$ is a valuation ring $\mathcal{O}_v \subsetneq K$ that contains $k$. It has a normalized valuation $\operatorname{ord}_v : K^\times \to \mathbb{Z}$ ([fields and extensions](/learn/algebra/#fields-and-extensions)).

**Definition 5.6.2 (Selmer group).** Let $K$ be a function field of one variable over $k$ and $q \ge 1$. The *Selmer group* of $K$ is
$$\operatorname{Sel}_q(K) = \{ f \in K^\times : q \mid \operatorname{ord}_v(f) \text{ for every place } v \}.$$
It contains $K^{\times q}$. We say that $\operatorname{Sel}_q(K)$ has *finitely many classes* if there is a finite set $T \subseteq K^\times$ such that each $f \in \operatorname{Sel}_q(K)$ is $t u^q$ with $t \in T$ and $u \in K^\times$.

If $k$ is algebraically closed and $C$ is the smooth projective curve with function field $K$, then $f \mapsto \operatorname{div}(f)/q$ identifies $\operatorname{Sel}_q(K)/K^{\times q}$ with $\operatorname{Pic}(C)[q]$. So the finiteness of the classes is a form of the finiteness of $q$-torsion in the Jacobian.

The next definitions describe the property that the previous section gives to a function field. For a field $L \supseteq k$ and a $k$-subalgebra $B \subseteq K$ we write $L \otimes B \to L \otimes K$ for the map $L \otimes_k B \to L \otimes_k K$; it is injective, since $L$ is flat over $k$.

**Definition 5.6.3 (Chart).** Let $K$ be a function field of one variable over $k$. A *chart* of $K$ is a $k$-subalgebra $B \subseteq K$ of finite type that is a Dedekind domain, not a field, with fraction field $K$, such that for each algebraically closed field $L \supseteq k$ the ring $L \otimes_k B$ is a Dedekind domain and not a field.

So a chart is the coordinate ring of an affine open part of the curve of $K$ that stays smooth over every algebraically closed $L$.

**Definition 5.6.4 (Enough charts).** Let $B$ be a chart of $K$, $L \supseteq k$ a field, $\mathfrak{m}$ a maximal ideal of $L \otimes_k B$ and $F \in L \otimes_k K$. Then $F$ is a *$q$-th power up to units at $\mathfrak{m}$* if there are $s, t \in (L \otimes_k B) \setminus \mathfrak{m}$ and nonzero $a, b \in L \otimes_k B$ with $F s b^q = t a^q$. The field $K$ has *enough charts for $q$* if there are finitely many charts $B_1, \dots, B_n$ with the following property. For each algebraically closed field $L \supseteq k$ and each nonzero $F \in L \otimes_k K$ that is a $q$-th power up to units at every maximal ideal of every $L \otimes_k B_i$, there are $f \in K^\times$ and nonzero $a, b \in L \otimes_k K$ with
$$F b^q = (1 \otimes f) \, a^q.$$

**Lemma 5.6.5 (Enough charts give finitely many classes).** Let $k$ be algebraically closed and $K$ a function field of one variable over $k$ with enough charts for $q$. Then $\operatorname{Sel}_q(K)$ has finitely many classes.

Lean: `UpperTheory.finite_kummerSelmer_of_charts`.

*Proof.* A separate result of the Lean code, whose proof we did not open, gives elements $v_1, \dots, v_n \in K$ such that each class of $\operatorname{Sel}_q(K)$ has a representative $\sum_i c_i v_i$ with $c \in k^n$. Consider the set of $c \in k^n$ for which $\sum_i c_i v_i$ lies in the Selmer group. The proof is a Noetherian induction on the closed subsets of $k^n$. For a prime ideal $I$ of $k[x_1, \dots, x_n]$, a second result works over the algebraic closure $L$ of the fraction field of $k[x_1, \dots, x_n]/I$, where the chart property applies. It gives a polynomial $g \notin I$ and a finite set of representatives for all $c$ in the zero set of $I$ with $g(c) \neq 0$. The rest of the zero set of $I$ is a smaller closed set, so the induction ends. $\square$

### Charts of a curve

**Theorem 5.6.6 (Charts of a curve).** Let $k$ be an algebraically closed field and $q$ an integer invertible in $k$. Let $C$ be an integral, proper and smooth curve over $k$ with function field $k(C)$. Then $k(C)$ is a function field of one variable over $k$ and has enough charts for $q$.

Lean: `UpperTheory.isFunctionField_and_charts_of_isCurve_of_isUnit`.

*Proof.* A result on curves, proved elsewhere in the Lean code, gives three things. First, $k(C)$ is a function field of one variable. Second, finitely many charts $B_1, \dots, B_n$ of $k(C)$, coordinate rings of affine open parts of $C$. Third, for each algebraically closed $L \supseteq k$, the base change $X = C_L$ with these properties: $X$ is integral and its local rings are integrally closed; there is an injective ring map $\theta : L \otimes_k k(C) \to L(X)$, compatible with $u : X \to C$; each element of $L(X)$ is a fraction $\theta(a)/\theta(b)$; and each point $y \in X$ lies over a prime ideal $\mathfrak{p}$ of some $L \otimes_k B_i$ such that each $s \notin \mathfrak{p}$ becomes a unit in $\mathcal{O}_{X,y}$.

Let $F \neq 0$ be a $q$-th power up to units at every maximal ideal of every $L \otimes_k B_i$. We show that $\theta(F)$ is locally a unit times a $q$-th power on $X$. Let $y \in X$, with $i$ and $\mathfrak{p}$ as above, and choose a maximal ideal $\mathfrak{m} \supseteq \mathfrak{p}$. The hypothesis at $\mathfrak{m}$ gives $s, t \notin \mathfrak{m}$ and $a, b \neq 0$ with $F s b^q = t a^q$. Then $s, t \notin \mathfrak{p}$, so $\theta(s)$ and $\theta(t)$ are units at $y$. Since $\theta$ and $L \otimes B_i \to L \otimes k(C)$ are injective, $\theta(a)$, $\theta(b)$ and $\theta(s)$ are nonzero, and
$$\theta(F) = \frac{\theta(t)}{\theta(s)} \left( \frac{\theta(a)}{\theta(b)} \right)^q.$$
Now [Theorem 5.5.2](/entry/base-change-curve-function-field-comp-of-normal/) (divisible divisors come from the curve) gives $f \in k(C)^\times$ and $h \in L(X)^\times$ with $\theta(F) = \theta(1 \otimes f) h^q$. Write $h = \theta(a)/\theta(b)$ with $b \neq 0$; then $a \neq 0$. So $\theta(F b^q) = \theta((1 \otimes f) a^q)$, and the injectivity of $\theta$ gives $F b^q = (1 \otimes f) a^q$. $\square$

### Finiteness of the Picard torsion

The theorem uses two results as hypotheses. Both are proved elsewhere in the Lean code.

1. *(Selmer to Picard.)* Let $B$ be a Dedekind domain with fraction field $K$, and let $\operatorname{sel}_q(B)$ be the group of $f \in K^\times$ whose principal fractional ideal is the $q$-th power of a fractional ideal. If $\operatorname{sel}_q(B)$ is finite modulo $q$-th powers of elements of $K^\times$, then the $q$-torsion of the class group of $B$ is finite. (If $I^q = (f)$, then $f \in \operatorname{sel}_q(B)$, and $f$ determines the class of $I$; this map from $\operatorname{sel}_q(B)$ onto the $q$-torsion is the reason.)
2. *(Model curve.)* Let $k$ be algebraically closed and let $K$ be a function field of one variable over $k$. Then there is an integral, proper and smooth curve $C_0$ over $k$ and a $k$-embedding $K \to k(C_0)$.

**Theorem 5.6.7 (Finite Picard torsion).** Assume statements 1 and 2. Let $k$ be an algebraically closed field, $q$ an integer invertible in $k$, and $B$ a Dedekind domain of finite type over $k$. Then $\operatorname{Pic}(B)[q]$ is finite.

Lean: `UpperTheory.curve_picard_of_selmerPicard_of_modelCurve`.

*Proof.* If $B$ is a field, then $\operatorname{Pic}(B)$ is trivial. Assume that $B$ is not a field, and let $K$ be its fraction field.

1. *Function field.* The ring $B$ has Krull dimension $1$ and is of finite type over $k$. So $K$ is a function field of one variable over $k$.
2. *A model.* Choose $u \in K$ transcendental over $k$ with $K$ finite over $k(u)$. Statement 2 gives a proper smooth curve $C_0$ and $K \subseteq k(C_0)$.
3. *Classes upstairs.* By the Theorem on charts of a curve, $k(C_0)$ has enough charts for $q$. By the Lemma, $\operatorname{Sel}_q(k(C_0))$ has finitely many classes.
4. *Descent.* A result of the Lean code, whose proof we did not open, states: if $K \subseteq K'$ are function fields of one variable over the algebraically closed field $k$, $q$ is invertible in $k$ and $\operatorname{Sel}_q(K')$ has finitely many classes, then so does $\operatorname{Sel}_q(K)$. So $\operatorname{Sel}_q(K)$ has finitely many classes.
5. *Back to $B$.* Only finitely many places $v$ of $K$ do not contain $B$: each of the finitely many generators of $B$ has nonzero order at only finitely many places. Let $S$ be this finite set. For $f \in \operatorname{sel}_q(B)$, the order $\operatorname{ord}_v(f)$ is divisible by $q$ at each place that contains $B$, since such a place is the localization at a maximal ideal of $B$. Choose one element $r(\epsilon) \in \operatorname{sel}_q(B)$ for each vector $\epsilon \in (\mathbb{Z}/q)^S$ of residues that occurs. Then $f / r(\epsilon(f))$ lies in $\operatorname{Sel}_q(K)$. With step 4, the class of $f$ modulo $q$-th powers is determined by $\epsilon(f)$ and by an element of the finite set $T$. So $\operatorname{sel}_q(B)$ is finite modulo $q$-th powers.
6. *Conclusion.* Statement 1 gives the finiteness of the $q$-torsion of the class group, which is $\operatorname{Pic}(B)[q]$. $\square$

**Remark 5.6.8.** The Lean theorem is an implication: statement 1 and statement 2 imply the finiteness statement. The finiteness statement itself also takes the bundle of 27 standing hypotheses on étale cohomology, which the proof passes to the Theorem on charts of a curve. The two statements are proved elsewhere and supplied in [EtaleTopology.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleTopology.lean#L162). Statement 2 gives an embedding $K \subseteq k(C_0)$, not an isomorphism; the descent in step 4 is the reason this is enough.
