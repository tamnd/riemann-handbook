---
title: A generating K-type of the real theta quotient
decls:
  - PositivityTheory.KReal.side_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A generating K-type of the real theta quotient

This section proves a fact on the Fock model of the dual pair $(U(p,q), U(r,s))$ at a real place. Take the largest quotient of the Fock space on which the [[Lie algebra|5JJYBJ6A8K]] of $U(p,q)$ acts by a character. We show that this quotient has one generating $K$-type for $U(r,s)$ with a known highest weight, and that the $K$-types one step above it have a larger Casimir value. The result gives the infinite places of [Theorem 2.6.4 of Volume 12](/entry/theorem-k-head2-of-mod/): two theta quotients with these data and the same highest weight have a common irreducible quotient. The Background for the Fock model is at [/learn/theta/#the-fock-model](/learn/theta/#the-fock-model), and for highest weights at [/learn/representations/#highest-weights-and-branching](/learn/representations/#highest-weights-and-branching).

Let $I_{r,s}$ be the disjoint union of $\{1, \dots, r\}$ and $\{1, \dots, s\}$. Two indices are in the same block if both are in the first part or both are in the second part. Write $a \prec b$ if $a$ and $b$ are in the same block and $a$ comes before $b$. Let $E_{ab}$ be the matrix units of $\mathfrak{gl}(I_{r,s}) = M_{r+s}(\mathbb{C})$, and let $\mathfrak{k} = \mathfrak{gl}_r \oplus \mathfrak{gl}_s$ be the span of the $E_{ab}$ with $a, b$ in the same block. Let $\mathcal{P}$ be the ring of polynomials in the variables $x_{ia}$, $i \in I_{p,q}$, $a \in I_{r,s}$, with the Fock inner product, and let $\mathcal{P}_d$ be its part of degree $d$. The Fock model gives two commuting Lie algebra maps $\omega_1 : \mathfrak{gl}(I_{p,q}) \to \mathrm{End}\,\mathcal{P}$ and $\omega_2 : \mathfrak{gl}(I_{r,s}) \to \mathrm{End}\,\mathcal{P}$. For $a, b$ in the same block, $\omega_2(E_{ab})$ keeps each $\mathcal{P}_d$, and $\langle \omega_2(E_{ab})u, v\rangle = \langle u, \omega_2(E_{ba})v\rangle$. For $a, b$ in different blocks, $\omega_2(E_{ab})$ is the sum of a raising part from $\mathcal{P}_d$ to $\mathcal{P}_{d+2}$ and a lowering part from $\mathcal{P}_d$ to $\mathcal{P}_{d-2}$. The same holds for $\omega_1$.

For $c \in \mathbb{C}$ let $\Theta_c$ be the quotient of $\mathcal{P}$ by the span of all $\omega_1(Z)P - c\,\mathrm{tr}(Z)P$, and let $\theta : \mathcal{P} \to \Theta_c$ be the quotient map. For $\tau \in \mathbb{C}$ and $W \in \mathfrak{gl}(I_{r,s})$ put $\omega_\tau(W)\theta(P) = \theta(\omega_2(W)P) + \tau\,\mathrm{tr}(W)\,\theta(P)$. As $\omega_1$ and $\omega_2$ commute, this is well defined. Let $\mathcal{P}_\chi$ be the space of $P$ with $\omega_1(Z)P = c\,\mathrm{tr}(Z)P$ for all $Z$ in the compact part $\mathfrak{gl}_p \oplus \mathfrak{gl}_q$, and let $\mathcal{H}$ be the joint harmonics: the $P$ that the lowering parts of all $\omega_1(Z)$ and $\omega_2(Z)$ with $Z$ off the blocks send to $0$.

For a family $\rho_{ab}$ of operators, $a, b$ in the same block, the Casimir operator is $C(\rho) = \sum \rho_{ab}\rho_{ba}$, the sum over all pairs in the same block. For a weight $\mu : I_{r,s} \to \mathbb{Q}$ put
$$c(\mu) = \sum_a \mu_a^2 + \sum_{a \prec b} (\mu_a - \mu_b).$$
If $\rho$ satisfies the relations of $\mathfrak{k}$ and $f$ is a highest weight vector of weight $\mu$, that is $\rho_{aa}f = \mu_a f$ and $\rho_{ab}f = 0$ for $a \prec b$, then $C(\rho)f = c(\mu)f$. For $\kappa \in \mathbb{Q}$ let $\mu^\kappa$ be $\mu - \kappa$ on the first block and $\mu + \kappa$ on the second block, and put $\deg_\kappa(\mu) = \sum_a |\mu^\kappa_a|$.

**Definition 2.8.1 (Joint shape).** Let $\mu$ be a weight on $I_{p,q}$ and $\mu'$ a weight on $I_{r,s}$. The pair has joint shape if there are decreasing lists $\alpha, \gamma$ of positive integers and $\beta, \delta$ of negative integers with $|\alpha| + |\beta| \le p$, $|\gamma| + |\delta| \le q$, $|\alpha| + |\delta| \le r$ and $|\gamma| + |\beta| \le s$, such that $\mu^{(r-s)/2}$ is $(\alpha, 0, \dots, 0, \beta)$ on the first block and $(\gamma, 0, \dots, 0, \delta)$ on the second, and $\mu'^{(p-q)/2}$ is $(\alpha, 0, \dots, 0, \delta)$ on the first block and $(\gamma, 0, \dots, 0, \beta)$ on the second.

Lean: `FockH1Action.JointShape` (also `FockH1Action.shiftNu`, `FockH1Action.degW`).

**Definition 2.8.2 (Admissible weight).** Let $c_0, \tau_0 \in \mathbb{Q}$ and let $\Lambda$ be a weight on $I_{r,s}$. Write $\underline{c_0}$ for the constant weight on $I_{p,q}$. Then $\Lambda$ is admissible if three conditions hold.
1. The pair $(\underline{c_0}, \Lambda)$ has joint shape.
2. $\Lambda$ is the only $\nu$ such that $(\underline{c_0}, \nu)$ has joint shape.
3. Let $\nu$ be a weight with $\nu_b \le \nu_a$ for $a \prec b$, with the support condition below, and with $\deg_{(p-q)/2}(\nu) = \deg_{(r-s)/2}(\underline{c_0}) + 2$. If $a, b$ are in different blocks and $\nu + e_a - e_b = \Lambda$, then $c(\Lambda + \tau_0) + r + s < c(\nu + \tau_0)$.

The support condition says: with positions counted from $0$, the entry of $\nu^{(p-q)/2}$ at position $k$ of the first block is at most $0$ if $k \ge p$ and at least $0$ if $k + q < r$, and the entry at position $l$ of the second block is at most $0$ if $l \ge q$ and at least $0$ if $l + p < s$.

Lean: `PositivityTheory.KReal.CombOK` (also `PositivityTheory.KReal.casW`, `PositivityTheory.KReal.Supp`).

**Definition 2.8.3 (Side data).** Let $T$ be a complex vector space with a linear map $\pi : \mathfrak{gl}(I_{r,s}) \to \mathrm{End}\,T$, and let $\Lambda$ be a weight. Then $T$ has side data of weight $\Lambda$ if $\pi$ is a Lie algebra map, $T \ne 0$, and there are a finite dimensional complex inner product space $A$, operators $\rho_{ab}$ of $A$, a linear map $\iota : A \to T$ and a vector $f \in A$ with the following properties, where $a, b, c, d$ run over pairs in the same block.
1. $\langle \rho_{ab}u, v\rangle = \langle u, \rho_{ba}v\rangle$.
2. $\rho_{ab}\rho_{cd} - \rho_{cd}\rho_{ab} = \delta_{bc}\rho_{ad} - \delta_{da}\rho_{cb}$.
3. $f$ is a highest weight vector of weight $\Lambda$ for $\rho$.
4. $\iota\rho_{ab} = \pi(E_{ab})\iota$.
5. The smallest $\pi$-stable subspace that contains $\iota(f)$ is $T$.
6. Let $t$ be real with $t \le c(\Lambda) + r + s$, and let $x$ be in the span of the $\pi(E_{ab})v$ with $a, b$ in different blocks and $v \in \iota(A)$. If $C(\pi)x = tx$, then $x = 0$.

Lean: `PositivityTheory.KReal.Side` (also `PositivityTheory.KReal.StarK`, `PositivityTheory.KReal.HwK`).

**Lemma 2.8.4 (Inputs).** Let $c_0 \in \mathbb{Q}$, $c = c_0$, and assume parts 1 and 2 of the admissibility of $\Lambda$. Put $d_0 = \deg_{(r-s)/2}(\underline{c_0})$.
1. $\omega_\tau$ is a Lie algebra map for every $\tau$.
2. There is a nonzero $f \in \mathcal{H} \cap \mathcal{P}_\chi \cap \mathcal{P}_{d_0}$ that is a highest weight vector of weight $\Lambda$ for $\omega_2|_{\mathfrak{k}}$, such that each $\mathfrak{k}$-stable subspace that contains $f$ contains $\mathcal{H} \cap \mathcal{P}_\chi$.
3. Let $N \subseteq \Theta_c$ be stable under $\omega_\tau$ and contain $\theta(\mathcal{H} \cap \mathcal{P}_\chi)$. Then $N = \Theta_c$.
4. If $d < d_0$, then $\theta(\mathcal{P}_d) = 0$, and $\theta(\mathcal{P}_{d_0+2}) = \theta(Y)$ with $Y = \mathcal{H}_1 \cap \mathcal{P}_\chi \cap \mathcal{P}_{d_0+2}$, where $\mathcal{H}_1$ are the harmonics for $\omega_1$ alone.
5. Let $g \in Y$ be a highest weight vector of weight $\nu$ for $\omega_2|_{\mathfrak{k}}$. Then $\nu$ satisfies the hypotheses of part 3 of admissibility for some $a, b$ in different blocks.

Lean: `PositivityTheory.KReal.lie_th` (also `PositivityTheory.KReal.exists_gen`, `PositivityTheory.KReal.th_gen_harm`, `PositivityTheory.KReal.th_small`, `PositivityTheory.KReal.th_next`, `PositivityTheory.KReal.root_of_hw`).

*Proof.* Part 1 follows from the Lie property of $\omega_2$ and from $\mathrm{tr}[X, Y] = 0$. For part 2, the theorem of Kashiwara and Vergne says that the joint harmonics that are highest weight vectors of weights $(\mu, \mu')$ form a line if $(\mu, \mu')$ has joint shape, and are $0$ otherwise. Let $f$ span the line for $(\underline{c_0}, \Lambda)$. Then $f \in \mathcal{P}_\chi$, and $f$ is homogeneous of degree $d_0$. Let $U$ be $\mathfrak{k}$-stable with $f \in U$, put $V = \mathcal{H} \cap \mathcal{P}_\chi$, which lies in $\mathcal{P}_{d_0}$, and let $Z$ be the orthogonal complement of $U \cap V$ in $V$. By the adjoint relation $Z$ is $\mathfrak{k}$-stable. If $Z \ne 0$, it contains a highest weight vector $g$ of some weight $\nu$. Then $(\underline{c_0}, \nu)$ has joint shape, so $\nu = \Lambda$ by uniqueness and $g \in \mathbb{C}f \subseteq U \cap V$. Thus $g \perp g$, so $g = 0$, which is false. So $Z = 0$ and $V \subseteq U$. For part 3, induct on the degree. Each $\mathcal{P}_d$ is the sum of its joint harmonics and of the raising parts applied to $\mathcal{P}_{d-2}$. The image of a $\mathfrak{gl}_p \oplus \mathfrak{gl}_q$-stable space in $\Theta_c$ is the image of its $\chi$-part, so the harmonic part maps into $N$. On $\Theta_c$, a matrix $Z$ off the blocks acts by $0$, so $\theta$ of the raising part of $\omega_1(Z)Q$ is $-\theta$ of its lowering part, which has degree $d - 4$ and lies in $N$ by induction. For the raising part of $\omega_2(Z)Q$, write it as $\omega_2(Z)Q$ minus its lowering part. By induction $\theta(Q)$ and $\theta$ of the lowering part are in $N$, and $N$ is $\omega_\tau$-stable, so it is in $N$. In degrees $0$ and $1$ all polynomials are joint harmonics. Parts 4 and 5 are computations in the Fock model with the same splitting and the degree bound for highest weight vectors. $\square$

**Theorem 2.8.5 (Side data of the theta quotient).** Let $c_0, \tau_0 \in \mathbb{Q}$, and let $\Lambda$ be admissible for $(p, q, c_0, \tau_0)$. If $\Theta_{c_0} \ne 0$, then $\Theta_{c_0}$ with $\omega_{\tau_0}$ has side data of weight $\Lambda + \tau_0$.

Lean: `PositivityTheory.KReal.side_of`.

*Proof.* Put $c = c_0$ and $\tau = \tau_0$. Take $d_0$ and $f$ from part 2 of the lemma. Let $A = \mathcal{P}_{d_0}$ with the Fock inner product. It is finite dimensional. For $a, b$ in the same block put $\rho_{ab} = \omega_2(E_{ab}) + \tau\delta_{ab}$ on $A$, and let $\iota$ be the restriction of $\theta$ to $A$. The Lie property is part 1, and $\Theta_c \ne 0$ is the hypothesis. Property 1 follows from the adjoint relation of $\omega_2$, since $\tau$ is real. Property 2 follows from part 1, because $[E_{ab}, E_{cd}] = \delta_{bc}E_{ad} - \delta_{da}E_{cb}$. For property 3, $\rho_{aa}f = (\Lambda_a + \tau)f$, and for $a \prec b$ we have $a \ne b$, so $\rho_{ab}f = \omega_2(E_{ab})f = 0$. Property 4 is the definition of $\omega_\tau$.

For property 5, let $N$ be the smallest $\omega_\tau$-stable subspace with $\theta(f) \in N$, and let $U = \theta^{-1}(N)$. Then $f \in U$. For $a, b$ in the same block and $x \in U$ we have $\theta(\omega_2(E_{ab})x) = \omega_\tau(E_{ab})\theta(x) - \tau\delta_{ab}\theta(x) \in N$, so $U$ is $\mathfrak{k}$-stable. By part 2 of the lemma, $\mathcal{H} \cap \mathcal{P}_\chi \subseteq U$, and by part 3, $N = \Theta_c$.

For property 6, let $t \le c(\Lambda + \tau) + r + s$ and let $x$ be as there with $C(\omega_\tau)x = tx$. For $a, b$ in different blocks, $\mathrm{tr}\,E_{ab} = 0$. So for $v \in \mathcal{P}_{d_0}$, $\omega_\tau(E_{ab})\theta(v)$ is $\theta$ of the raising part, of degree $d_0 + 2$, plus $\theta$ of the lowering part, of degree $d_0 - 2$. The second term is $0$ by part 4. So $x \in \theta(\mathcal{P}_{d_0+2})$, and by part 4, $x = \theta(y)$ with $y \in Y$. The space $Y$ is finite dimensional and stable under $\omega_2|_{\mathfrak{k}}$, so it is stable under $D = C(\rho^\tau) - t$, where $\rho^\tau_{ab} = \omega_2(E_{ab}) + \tau\delta_{ab}$ on $\mathcal{P}$. The map $\theta$ takes $D$ to $C(\omega_\tau) - t$.

We show that $D$ is injective on $Y$. If not, $U' = Y \cap \ker D$ is a nonzero finite dimensional space. The Casimir operator commutes with $\mathfrak{k}$, so $U'$ is $\mathfrak{k}$-stable and contains a highest weight vector $g$ of some weight $\nu$ for $\omega_2|_{\mathfrak{k}}$. By part 5 of the lemma and part 3 of admissibility, $c(\Lambda + \tau) + r + s < c(\nu + \tau)$. But $g$ is a highest weight vector of weight $\nu + \tau$ for $\rho^\tau$, so $0 = Dg = (c(\nu + \tau) - t)g$ and $c(\nu + \tau) = t \le c(\Lambda + \tau) + r + s$. This is a contradiction.

Now let $Z = Y \cap \ker\theta$. It is finite dimensional and $D$-stable, because $\theta(Dz) = (C(\omega_\tau) - t)\theta(z) = 0$. As $D$ is injective on $Z$, it is onto $Z$. We have $Dy \in Y$ and $\theta(Dy) = (C(\omega_\tau) - t)x = 0$, so $Dy \in Z$, and $Dy = Dz$ for some $z \in Z$. Injectivity on $Y$ gives $y = z$, so $x = \theta(y) = 0$. $\square$

The theorem is used twice, for the theta quotients from $U(p,q)$ and from a second group $U(p',q')$, with the same $U(r,s)$ and the same weight $\Lambda + \tau_0$. Properties 1 to 6 then give a common quotient of the two theta quotients that is nonzero and irreducible.

**Remark 2.8.6 (Formalization).** The theorem `side_of` is in [CoreSide.lean](lean:Development/WeilBound/CoreStatements/GaussianSeminormBounds/RealSeminormFiltration/CoreSide.lean#L159). The statements `Side` and `CombOK` are in [CoreDefs.lean](lean:Development/WeilBound/CoreStatements/GaussianSeminormBounds/RealSeminormFiltration/CoreDefs.lean#L66), and the quotient `ThC` with the subspace `polChi` is in [RealTh.lean](lean:Formalism/LocalToGlobal/ThetaOperatorCommutation/RealTh.lean#L24). The space $A$ is `sd_hA`, the operators $\rho$ are `sd_rhoA`, and property 6 is `star_th` in [CoreStar.lean](lean:Development/WeilBound/CoreStatements/GaussianSeminormBounds/RealSeminormFiltration/CoreStar.lean#L77). The user is `coreLM` in [CoreLM.lean](lean:Development/WeilBound/CoreStatements/GaussianSeminormBounds/RealSeminormFiltration/CoreLM.lean#L14), which applies `side_of` twice and then `common_quot`. Some points of the code:
- `side_of` takes $c, \tau \in \mathbb{C}$ and $c_0, \tau_0 \in \mathbb{Q}$ with the hypotheses `hc : c = c0` and `hτ : τ = τ0`. The complex values only carry the rational ones, and `coreLM` must build the casts `c1` and `c2` for them.
- In `sd_rhoA` (CoreSide.lean, line 90) the operators are $0$ for $a, b$ in different blocks. The branch of the proof for $a \prec b$ in different blocks (line 187) cannot occur, since $\prec$ holds only in one block.
- `sd_trace_Eab` (line 15) and `sd_sb_refl` (line 28) repeat `star_trace` and `star_sb_refl` of CoreStar.lean (lines 51 and 74).
- The highest weight condition `HwK` does not ask $f \ne 0$. Property 5 with $T \ne 0$ gives it.

## Notes and references

The chapter feeds three parts of the proof. The closed form of the congruence length bound is the main input of [the Selmer bound at a point](/entry/selmer-bound-at-point-main/) in Volume 4. The window bound from counts gives the statement VWin of [the proof chapter on VWin](/proof/vwin/) through [the theorem with four counts](/entry/of-four-alt/) in Volume 9. The local facts of the last three sections are inputs of [Theorem 2.6.4 of Volume 12](/entry/theorem-k-head2-of-mod/) in Volume 12, and all of them lie below the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/).

- R. Howe, *θ-series and invariant theory*, Proc. Sympos. Pure Math. 33 (1979), Part 1, for the Fock model, the joint harmonics and Howe duality at the unramified places.
- M. Kashiwara and M. Vergne, *On the Segal-Shale-Weil representations and harmonic polynomials*, Invent. Math. 44 (1978), for the joint shape of the highest weights of joint harmonics.
- A. W. Knapp, *Lie Groups Beyond an Introduction*, Chapter IV, for compact groups, $K$-finite vectors and the Casimir value of a highest weight.
- J.-P. Serre, *Local Fields*, Chapter IV, §2, for ramification groups and wild inertia.
- J. Neukirch, A. Schmidt and K. Wingberg, *Cohomology of Number Fields*, Chapter VIII, for the Selmer groups and the Poitou-Tate sequence.
- J. S. Milne, *Arithmetic Duality Theorems*, Chapter I, for local Tate duality and the Euler characteristic formula.
