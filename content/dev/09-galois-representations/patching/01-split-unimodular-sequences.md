---
title: Split unimodular sequences
decls:
  - GlobalTheory.SeqCx.splitAcyclic_step
  - GlobalTheory.T.splitSeq_exactAt_of_two_mul_add_stableRange_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Split unimodular sequences

This section proves that the complex of split unimodular sequences in $R^n$ is acyclic in a range that depends on the stable range of $R$. The group $\mathrm{GL}_n(R)$ acts on this complex, and the next section uses it to prove homological stability for $\mathrm{GL}_n(R)$. That stability result is one input of Lemma K in the [window bound](/proof/vwin/). The method is the one of Quillen and van der Kallen: an induction on $n$, in which a double complex compares split sequences with plain unimodular sequences. The background is in [rings, ideals and modules](/learn/algebra/#rings-ideals-and-modules) and [matrices](/learn/algebra/#matrices).

### Stable range

Let $R$ be a commutative ring and $n \ge 0$. Write $x \cdot y = \sum_i x_i y_i$ for $x, y \in R^n$. A vector $r \in R^n$ is *unimodular* if its entries generate the unit ideal, that is, if there is $f \in R^n$ with $f \cdot r = 1$. Equivalently, $r$ spans a free direct summand of $R^n$.

**Definition 7.1.1 (Stable range).** Let $s \ge 0$. The ring $R$ has *stable range at most $s$* if for each $n \ge s$ and each unimodular $r = (r_1, \dots, r_{n+1}) \in R^{n+1}$ there is $t \in R^n$ such that the vector $(r_1 + t_1 r_{n+1}, \dots, r_n + t_n r_{n+1}) \in R^n$ is unimodular.

The condition says that a unimodular vector can be shortened by elementary operations once it is long enough. This is the stable range condition of Bass. For example, a field $k$ has stable range at most $1$. Let $n \ge 1$ and $r \in k^{n+1}$ be nonzero. If some $r_i$ with $i \le n$ is nonzero, take $t = 0$. Otherwise $r_{n+1} \ne 0$, and $t = (r_{n+1}^{-1}, 0, \dots, 0)$ makes the first entry equal to $1$. The application in the next section uses a ring of integers of a number field, which has stable range at most $2$ by a theorem of Bass.

### The complexes

For a set $F$ of finite sequences of elements of a set $V$, let $C_p(F)$ be the free abelian group on the sequences in $F$ of length $p$. The *deletion differential* is
$$\partial (x_1, \dots, x_p) = \sum_{i=1}^{p} (-1)^{i-1} (x_1, \dots, \widehat{x_i}, \dots, x_p).$$
If $F$ is closed under taking subsequences, then $\partial$ maps $C_p(F)$ to $C_{p-1}(F)$ and $\partial^2 = 0$. The empty sequence spans $C_0(F)$, so the complex is augmented. We say that $F$ is *exact at $p$* if each $c \in C_p(F)$ with $\partial c = 0$ is $\partial b$ for some $b \in C_{p+1}(F)$.

**Definition 7.1.2 (Unimodular and split sequences).** Let $R$ be a commutative ring and $n \ge 0$.

1. A sequence $(v_1, \dots, v_p)$ of vectors in $R^n$ is *unimodular* if there are $f_1, \dots, f_p \in R^n$ with $f_i \cdot v_j = \delta_{ij}$. Write $U(R^n)$ for the set of these sequences.
2. A *split sequence* in $R^n$ is a sequence of pairs $((v_1, f_1), \dots, (v_p, f_p))$ in $R^n \times R^n$ with $f_i \cdot v_j = \delta_{ij}$ for all $i, j$. Write $S(R^n)$ for the set of these sequences.

A unimodular sequence of length $p$ is a basis of a free direct summand of rank $p$. A split sequence also fixes a complement: the common kernel of $f_1, \dots, f_p$. Both sets are closed under subsequences. The group $\mathrm{GL}_n(R)$ acts on $S(R^n)$ by $g(v, f) = (gv, (g^{T})^{-1} f)$, and this action preserves the conditions $f_i \cdot v_j = \delta_{ij}$.

We use one fact on $U$. It is proved by the same kind of link argument, and we do not reproduce the proof.

**Theorem 7.1.3 (Exactness for unimodular sequences).** Let $R$ have stable range at most $s$. If $q + s \le m$, then $U(R^m)$ is exact at $q$. More generally, let $\rho = ((v_1, f_1), \dots, (v_a, f_a))$ be a split sequence in $R^N$ with $a + m = N$ and $s \le m$. If $U(R^m)$ is exact at $q$, then the set of unimodular sequences $(u_1, \dots, u_b)$ in $R^N$ with $f_i \cdot u_j = 0$ for all $i, j$ is exact at $q$.

Lean: `GlobalTheory.T.unimodularSeqComplex_exactAt_of_add_stableRank_le`, `GlobalTheory.T.exactAt_uniSeq_orthogonal_splitSeq_of_exactAt_uniSeq`.

The second part reduces to the first: the common kernel of the $f_i$ is a free module of rank $m$, and a unimodular sequence in it is the same as a unimodular sequence in $R^N$ that the $f_i$ kill.

### Acyclicity

**Theorem 7.1.4 (Acyclicity of split sequences).** Let $R$ be a commutative ring of stable range at most $s$. If $2p + s + 1 \le n$, then $S(R^n)$ is exact at $p$.

Lean: `GlobalTheory.T.splitSeq_exactAt_of_two_mul_add_stableRange_le`.

The proof is an induction on $n$. Its step is the following lemma.

**Lemma 7.1.5 (Inductive step).** Let $R$ have stable range at most $s$, and let $n \ge 0$. Suppose that $S(R^{n'})$ is exact at $p'$ whenever $n' < n$ and $2p' + s + 1 \le n'$. If $2p + s + 1 \le n$, then $S(R^n)$ is exact at $p$.

Lean: `GlobalTheory.SeqCx.splitAcyclic_step`.

*Proof.* Let $P$ be the set of pairs $(\sigma, w)$, where $\sigma = ((v_1, f_1), \dots, (v_a, f_a))$ is a split sequence in $R^n$, $w = (u_1, \dots, u_b)$ is a unimodular sequence in $R^n$, and $f_i \cdot u_j = 0$ for all $i, j$. The set $P$ is closed under subsequences in each coordinate. Let $C_{a,b}$ be the free abelian group on the pairs with $|\sigma| = a$ and $|w| = b$. Deletion in $\sigma$ gives a horizontal differential $\partial^h \colon C_{a,b} \to C_{a-1,b}$, and deletion in $w$ gives a vertical differential $\partial^v \colon C_{a,b} \to C_{a,b-1}$. They commute, and each squares to zero, so $C$ is a double complex.

Let $c \in C_p(S(R^n))$ be a cycle. Pairing each sequence with the empty sequence $w = ()$ makes $c$ an element of $C_{p,0}$, and it is a cycle for both differentials.

Columns. Fix $\sigma$ of length $a$. The sequences $w$ with $(\sigma, w) \in P$ are the unimodular sequences killed by the forms of $\sigma$. By the theorem on unimodular sequences with $N = n$ and $m = n - a$, this set is exact at $b$ when $b + s \le n - a$. For $a + b = p$ this holds, since $p + s \le 2p + s + 1 \le n$.

Rows. Fix a unimodular $w$ of length $b \ge 1$. The split sequences $\sigma$ with $(\sigma, w) \in P$ are those whose forms kill $w$. Complete $w$ to a split sequence $\gamma$ by a choice of forms. A standard link argument reduces exactness of this set at $a$ to exactness of the links of its simplices, and each such link is identified with the link of a split sequence $\rho$ in $S(R^n)$, which is a complex of split sequences in the complement of $\rho$, of rank $n - |\rho| < n$. The induction hypothesis then shows that the set is exact at $a$ when $2a + b + s + 1 \le n$. For $a + b = p + 1$ and $b \ge 2$ this holds, since $2a + b = 2(p + 1) - b \le 2p$.

Staircase. The usual staircase argument in a double complex, with exact columns on the diagonal $a + b = p$ and exact rows on the diagonal $a + b = p + 1$ below row $2$, gives $z \in C_{p,1}$ with $\partial^v z = c$ and $\partial^h z = 0$. Write $z = \sum_u z_u$, where $z_u$ collects the terms with $w = (u)$. Then each $z_u$ is a cycle in the complex of split sequences whose forms kill the unimodular vector $u$. Since $2p + s + 1 \le n$, such a cycle is a boundary. To see this, choose $f$ with $f \cdot u = 1$. The link argument and the induction hypothesis move $z_u$, up to a boundary, into the subcomplex of sequences whose vectors are also killed by $f$. On that subcomplex, putting the pair $(u, f)$ in front of each sequence is a cone, so the moved cycle is a boundary. This gives $z_u = \partial^h y_u$ with $y_u \in C_{p+1,1}$. Put $y = \sum_u y_u$. Then $c = \partial^v \partial^h y = \partial^h \partial^v y$, and $\partial^v y$ lies in $C_{p+1,0} = C_{p+1}(S(R^n))$. So $c$ is a boundary. $\square$

*Proof of the theorem.* By strong induction on $n$, the lemma gives exactness of $S(R^n)$ at each $p$ with $2p + s + 1 \le n$. $\square$

**Remark 7.1.6.** For $p = 0$ the theorem says that $S(R^n)$ is not empty in length $1$ when $s + 1 \le n$. For a field, $s = 1$, and the theorem gives exactness at $p$ for $n \ge 2p + 2$.

**Remark 7.1.7 (Formalization).** The theorem appears twice: once as the strong induction `GlobalTheory.SeqCx.exactAt_splitSeq_of_stableRange` ([SplitSeqExactAtOfTwoMulAddStableRangeLe.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/HomologicalStability/LinkExactnessStability/SplitSeqExactAtOfTwoMulAddStableRangeLe.lean#L73)), and once as the root theorem at line 83, whose proof is `first | exact … | exact @splitAcyclic_step`. The second branch has the wrong type and is never used. The helper lemmas of this section have the same `first` wrappers. The exactness of $U(R^m)$ and the row exactness are separate lemmas of the same folder; this section states their content and does not reprove them.
