---
title: Frame degrees at root origins
decls:
  - GlobalTheory.T.root_origin_frame_degree_bound
  - GlobalTheory.CompanionTheory.Ar.Rec.FinRd.Roots.reads_roots
  - GlobalTheory.CompanionTheory.Ar.Rec.FinRd.Roots.diag_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Frame degrees at root origins

At a finite place the generic frame of a root origin and the Lie model of an integral point give two lattices in the same fibre. This section proves that they agree up to a bounded power of $p$, and it turns this into a statement on the values of the root sections at small $\overline{\mathbb{Q}}_p$ points. The exponent of the defect is the constant $c_p$ of the earlier sections. The result is the finite part of the [uniform bound at all root origins](/entry/relay-uniform-all-root-origin-bound/) of the section on descent of small sections, where it is the input at the primes of $S$.

We keep the setting of that section. We assume the top level inputs. $E$ is a CM field that is Galois over $\mathbb{Q}$, with host $H$, a datum $D$ with $N = p + q$, a level, a moduli space, a coefficient datum with number field $F$, and a model $Y$ over $\mathcal{O}_F$. $S$ is a finite set of primes that contains every prime that divides $d_E$. $R$ is a root model with ring of functions $\Omega$, with coordinates $y_{k,i}$, and $O$ is a root origin over $S$ with generic frame $\mathrm{Fr}$. We assume that the Hodge bundle of $O$ has the vector bundle property.

### The exponent

For a prime $p$ put
$$
h_p = \begin{cases} 2 & p = 2, \\ \frac{1}{p-1} & p \ne 2, \end{cases}
$$
and
$$
c_p = \begin{cases} h_p + \frac{v_p(d_E)}{[E:\mathbb{Q}]} & p \in S, \\ 0 & p \notin S. \end{cases}
$$
The first term comes from the ramification of the $p$-adic logarithm, and it is the term that bounds the denominators of the Lie model over a ramified ring. The second term is the different of $E$ at $p$, divided by the degree.

**Definition 8.16.1 (Reads roots).** Let $p$ be a prime, let $z$ be a $\overline{\mathbb{Q}}_p$ point of the coordinate ideal of $R$ with algebraic coordinates, let $t$ assign a nonzero number to each frame index, and let $\theta \ge 0$. We say that $z$ reads the roots of $O$ up to $\theta$ for $t$ if for each root index $\rho$ there is $w \ne 0$ in $\overline{\mathbb{Q}}_p$ such that the root section $e_\rho^{-1}$ of degree $\deg \rho$ has the value $w$ at $z$, and
$$
\Bigl| \log \sup_{\deg \rho}(z) - \log \frac{\| w \|}{t_{i(\rho)}^{\epsilon(\rho)}} \Bigr| \le \theta \log p .
$$
Here $i(\rho)$ is the frame index of $\rho$, $\epsilon(\rho) = \pm 1$ is its sign, and
$$
\sup_a(z) = \prod_k \bigl\| (z_{k,i})_i \bigr\|^{a_k}
$$
is the sup metric of the weight $a$.

So the condition says that, on the small point $z$, the norm of a root section is the sup norm of its weight, up to the ratio of the frame of $t$ and up to $p^{\theta}$.

### A comparison of lattices

Fix a prime $p$ and an integral point: a prime $\lambda$ of $\mathcal{O}_F$ over $p$, a complete discrete valuation ring $T$ with fraction field $K$, an embedding $F \to K$, an integral frame, and units $t_j \in K^\times$ for the frame indices. Over $T$ there is a Lie model $M$ with an action of $\mathcal{O}_E$, and for each CM label $s$ the $s$ eigen part of its Lie algebra is a lattice $\Lambda_s$ in the fibre $V_s$ of the Hodge bundle at the point.

**Lemma 8.16.2 (Comparison of eigen lattices).** Let $\sigma: \mathcal{O}_E \to T$ match the embedding of the label $s$. There are $d, d' \in T$ with
$$
\begin{aligned}
d \, \Lambda_s &\subseteq V_s(\mathcal{O}), \\
d' \, V_s(\mathcal{O}) &\subseteq \Lambda_s,
\end{aligned}
$$
and $p^{-c_p} \le |d|$ and $p^{-c_p} \le |d'|$. If $p \notin S$ one can take $d = d' = 1$.

*Proof.* If $p \notin S$, the combined frame result at root origins says that the two lattices are equal, so $d = d' = 1$. If $p \in S$, the total bound at root origins and the height estimate at root origins give the two inclusions with constants of absolute value at least $p^{-c_p}$. The first bound controls the denominators of the formal logarithm, which gives $h_p$. The second controls the eigen decomposition of $\mathcal{O}_E \otimes T$, which is not a product of copies of $T$ when $p$ ramifies in $E$; the defect is the different, which gives $v_p(d_E)/[E:\mathbb{Q}]$. $\square$

### The diagonal bound

Let $A \subseteq \Omega$ be a subring that is good for the generic frame, so that the frame vectors of $\mathrm{Fr}$ have coefficients in $A$, and that contains the ratios $y_{k,i}/y_{k,j}$. Let $\mathrm{ev}: A \to \overline{\mathbb{Q}}_p$ be the evaluation at $z$, and let $\mathrm{ev}_T$ be the evaluation at the integral point.

**Lemma 8.16.3 (Diagonal bound).** Let $s$ be a label, and let $b$ be a basis of the Lie bundle of $O$ with the same flag steps as the frame $\mathrm{Fl}_s$. Assume that $b$ is a frame at the centre of the integral point, and write $b = T_m \, \mathrm{Fl}_s$ with entries of $T_m$ in $A$. If $\mathrm{ev}_T(T_{m,ii}) \ne 0$, then
$$
\Bigl| \log \bigl| \mathrm{ev}_T(T_{m,ii}) \bigr| - \log \bigl| t_{j(s,i)} \bigr| \Bigr| \le c_p \log p ,
$$
where $j(s,i)$ is the frame index of the pair $(s, i)$.

Lean: `GlobalTheory.CompanionTheory.Ar.Rec.FinRd.Roots.diag_bound`.

*Proof.* The two bases have the same flag steps, so the change of basis is lower triangular. On the diagonal, the coefficient $T_{m,ii}$ is the ratio of the $i$th graded pieces of the two flags. The coefficient of a triangular span is the ratio of the last coordinates, so we can read $T_{m,ii}$ on the graded piece of $V_s$ of index $i$.

The frame $b$ at the integral point spans the lattice $V_s(\mathcal{O})$ of the Hodge bundle, and the units $t$ span, by the definition of an integral frame, the lattice that comes from the Lie model, which is $\Lambda_s$ in each graded step. The lemma on eigen lattices gives $d$ and $d'$ for the two inclusions. On the graded piece of index $i$, these inclusions give
$$
\begin{aligned}
|d| \, |t_{j(s,i)}| &\le |\mathrm{ev}_T(T_{m,ii})| , \\
|d'| \, |\mathrm{ev}_T(T_{m,ii})| &\le |t_{j(s,i)}| .
\end{aligned}
$$
With $|d|, |d'| \ge p^{-c_p}$ we get the two sides of the bound. The local bound and the relay bound at root origins give the passage from the lattice over the complete ring to the finite residue absolute value, and the archimedean frame bound gives nothing at $p$, so the bound holds as stated. $\square$

### Values of root sections

**Theorem 8.16.4 (Frame degree bound at root origins).** Assume the top level inputs, and let $E$, $S$, $R$, $O$ and $\mathrm{Fr}$ be as above. Let $p$ be a prime, let $z$ be a $\overline{\mathbb{Q}}_p$ point of the coordinate ideal of $R$ with algebraic coordinates, and let $A$ and $\mathrm{ev}$ be as above. Let an integral point be given by $\lambda$, $T$, an integral frame and units $t$, such that it specializes to $z$. Then $z$ reads the roots of $O$ up to $c_p$ for the units $t$.

Lean: `GlobalTheory.T.root_origin_frame_degree_bound` (also `GlobalTheory.CompanionTheory.Ar.Rec.FinRd.Roots.reads_roots`, a second name).

*Proof.* Fix a root index $\rho$. A root section $e_\rho^{-1}$ is a product of a minor $M_\rho$ of the frame matrix of $\mathrm{Fr}$ and a monomial in the coordinates. For each $k$ choose an index $\mathrm{ch}(k)$ with $z_{k, \mathrm{ch}(k)} \ne 0$ and $|z_{k,\mathrm{ch}(k)}| = \| (z_{k,i})_i \|$. Put
$$
w = \mathrm{ev}(M_\rho) \prod_k z_{k, \mathrm{ch}(k)}^{\deg \rho_k} .
$$
The ratios $y_{k,i}/y_{k,\mathrm{ch}(k)}$ lie in $A$, so the specialization of coordinate ratios at $z$ and at the integral point shows that $w$ is the value of $e_\rho^{-1}$ at $z$. The norm of the monomial is $\sup_{\deg \rho}(z)$, by the choice of $\mathrm{ch}(k)$.

It remains to bound $|\mathrm{ev}(M_\rho)|$. The minor $M_\rho$ is, up to sign, a diagonal entry $T_{m,ii}$ of the change of basis of the diagonal lemma, or its inverse; this is the sign $\epsilon(\rho)$. The root index bound at root origins gives the label and the step $i$ that belong to $\rho$. The values at $z$ and at the integral point agree, by the comparison of the finite residue absolute values, so $\mathrm{ev}_T(T_{m,ii}) \ne 0$ and the diagonal lemma applies. It gives
$$
\bigl| \log |\mathrm{ev}(M_\rho)|^{\epsilon(\rho)} - \log |t_{i(\rho)}| \bigr| \le c_p \log p .
$$

Now we use a small rule on logarithms. If $m = x^n$ with $n = \pm 1$, and $|\log x - \log y| \le \theta$, then for every $S > 0$
$$
\Bigl| \log S - \log \frac{S}{m \, y^{-n}} \Bigr| \le \theta .
$$
We apply it with $S = \sup_{\deg \rho}(z) \cdot |\mathrm{ev}(M_\rho)|$, $m = |\mathrm{ev}(M_\rho)|$, $y = |t_{i(\rho)}|$ and $n = \epsilon(\rho)$. The value of the regular function at $z$ is the regular value of the specialization, used twice: once for the minor and once for the monomial. Together this gives the inequality of the definition with $\theta = c_p$. $\square$

So at a prime outside $S$ the small points read the root sections exactly, and at a prime of $S$ they read them up to $p^{c_p}$. The sum of $c_p \log p$ over $p \in S$ is the finite cost in the uniform bound at all root origins.

**Remark 8.16.5 (Formalization).** The statement file RootOriginFrameDegreeBoundStatement.lean imports `Mathlib` twice (lines 1 and 3), and the theorem is a renaming of `reads_roots` proved by `first | exact @...` under `maxHeartbeats 1000000`. The proof file RootOriginFrameDegreeBound.lean has 338 lines; `reg_val` (line 31), `log_bound` (line 39), the comparison `compare` (line 59), `diag_bound` (line 102) and `reads_roots` (line 188) are in it. The comparison of eigen lattices is the private lemma `compare`; it has no name in the outline, and in the case $p \notin S$ it uses the equality from `root_origin_frame_combined` with $d = d' = 1$. The exponent `latExp` puts $2$ at $p = 2$ in `htExp`, where the formula $\frac{1}{p-1} + 1$ of earlier sections also gives $2$. The witness $w$ is the product of the evaluated minor and the monomial in the chosen coordinates (line 188 plus 129). We do not unfold the root model, the generic frame or the Lie model.
